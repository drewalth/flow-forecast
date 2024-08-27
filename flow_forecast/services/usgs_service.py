import datetime
import json
import numpy as np
import pandas as pd
import urllib3

default_start_date = datetime.date(1888, 1, 1)
default_end_date = datetime.date(2100, 12, 31)
default_parameter = "00060"  # cubic feet per second (cfs)
base_usgs_url = "http://waterservices.usgs.gov/nwis/dv/?format=json"


def get_daily_average_data(
    site_id: str,
    start_date: datetime.date = default_start_date,
    end_date: datetime.date = default_end_date,
    gauge_parameter: str = default_parameter,
) -> dict:
    """Calls USGS api to get daily average values in the given date range"""

    url = f"{base_usgs_url}&site={site_id}&startDT={start_date}&endDT={end_date}&parameterCd={gauge_parameter}"  # noqa: E501
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    response_json = json.loads(response.data.decode("utf-8"))
    # may have to change this if the json format is different
    return response_json["value"]["timeSeries"][0]["values"][0]["value"]


def clean_data(json_data: dict) -> pd.DataFrame:
    """Given usgs json data, cleans the data and returns a DataFrame"""

    df = pd.DataFrame(json_data)
    df = df.drop("qualifiers", axis=1)
    df["value"] = df["value"].astype(float)
    df["dateTime"] = pd.to_datetime(df["dateTime"])
    df.set_index("dateTime", inplace=True)
    df = df.asfreq("d")  # adds missing day data
    df.loc[df["value"] <= 0, "value"] = np.nan
    df = df.reset_index()
    df = df[["dateTime", "value"]]
    return df


def format_season_average_data(json_data: dict) -> pd.DataFrame:
    """Given USGS data, cleans the data and formats to display seasonal averages"""

    df = pd.DataFrame(json_data)
    df = df.drop("qualifiers", axis=1)
    df["value"] = df["value"].astype(float)
    df["dateTime"] = pd.to_datetime(df["dateTime"])
    months, days, years = zip(*[(d.month, d.day, d.year) for d in df["dateTime"]])
    df = df.assign(month=months, day=days, year=years)
    df = df.drop("dateTime", axis=1)
    df = df.pivot(index=["month", "day"], columns="year", values="value")
    df.index = df.index.map(lambda t: f"{t[0]}/{t[1]}")
    df[df <= 0] = np.nan
    return df