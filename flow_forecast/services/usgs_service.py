# import datetime
# import json

# import numpy as np
# import pandas as pd
# import urllib3

# base_usgs_url = "http://waterservices.usgs.gov/nwis/dv/?format=json"


# def get_daily_average_data(
#     site_id: str,
#     reading_parameter: str,
#     start_date: datetime.date,
#     end_date: datetime.date,
# ) -> list[dict]:
#     """Calls USGS api to get daily average values in the given date range"""
#     url = f"{base_usgs_url}&site={site_id}&startDT={start_date}&endDT={end_date}&parameterCd={reading_parameter}"  # noqa: E501

#     http = urllib3.PoolManager()
#     response = http.request("GET", url)
#     response_json = json.loads(response.data.decode("utf-8"))
#     # may have to change this if the json format is different
#     return response_json["value"]["timeSeries"][0]["values"][0]["value"]


# def clean_data(json_data: dict) -> pd.DataFrame:
#     """Given usgs json data, cleans the data and returns a DataFrame"""

#     data_frame = pd.DataFrame(json_data)
#     data_frame = data_frame.drop("qualifiers", axis=1)
#     data_frame["value"] = data_frame["value"].astype(float)
#     data_frame["dateTime"] = pd.to_datetime(data_frame["dateTime"])
#     data_frame.set_index("dateTime", inplace=True)
#     data_frame = data_frame.asfreq("d")  # adds missing day data
#     data_frame.loc[data_frame["value"] <= 0, "value"] = np.nan
#     data_frame = data_frame.reset_index()
#     data_frame = data_frame[["dateTime", "value"]]
#     return data_frame


# def format_season_average_data(json_data: dict) -> pd.DataFrame:
#     """Given USGS data, cleans the data and formats to display seasonal averages"""

#     data_frame = pd.DataFrame(json_data)
#     data_frame = data_frame.drop("qualifiers", axis=1)
#     data_frame["value"] = data_frame["value"].astype(float)
#     data_frame["dateTime"] = pd.to_datetime(data_frame["dateTime"])
#     months, days, years = zip(*[(d.month, d.day, d.year) for d in data_frame["dateTime"]])
#     data_frame = data_frame.assign(month=months, day=days, year=years)
#     data_frame = data_frame.drop("dateTime", axis=1)
#     data_frame = data_frame.pivot(index=["month", "day"], columns="year", values="value")
#     data_frame.index = data_frame.index.map(lambda t: f"{t[0]}/{t[1]}")
#     data_frame[data_frame <= 0] = np.nan
#     return data_frame
