import datetime
import datetime as dt
import json
import logging

import numpy as np
import pandas as pd
import urllib3
from prophet import Prophet

base_usgs_url = "http://waterservices.usgs.gov/nwis/dv/?format=json"

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def get_daily_average_data(
    site_id: str,
    reading_parameter: str,
    start_date: datetime.date,
    end_date: datetime.date,
) -> list[dict]:
    """Calls USGS api to get daily average values in the given date range"""
    url = f"{base_usgs_url}&site={site_id}&startDT={start_date}&endDT={end_date}&parameterCd={reading_parameter}"  # noqa: E501

    http = urllib3.PoolManager()
    response = http.request("GET", url)
    response_json = json.loads(response.data.decode("utf-8"))
    # may have to change this if the json format is different
    return response_json["value"]["timeSeries"][0]["values"][0]["value"]


def clean_data(json_data: dict) -> pd.DataFrame:
    """Given usgs json data, cleans the data and returns a DataFrame"""

    data_frame = pd.DataFrame(json_data)
    data_frame = data_frame.drop("qualifiers", axis=1)
    data_frame["value"] = data_frame["value"].astype(float)
    data_frame["dateTime"] = pd.to_datetime(data_frame["dateTime"])
    data_frame.set_index("dateTime", inplace=True)
    data_frame = data_frame.asfreq("d")  # adds missing day data
    data_frame.loc[data_frame["value"] <= 0, "value"] = np.nan
    data_frame = data_frame.reset_index()
    data_frame = data_frame[["dateTime", "value"]]
    return data_frame


def format_season_average_data(json_data: dict) -> pd.DataFrame:
    """Given USGS data, cleans the data and formats to display seasonal averages"""

    data_frame = pd.DataFrame(json_data)
    data_frame = data_frame.drop("qualifiers", axis=1)
    data_frame["value"] = data_frame["value"].astype(float)
    data_frame["dateTime"] = pd.to_datetime(data_frame["dateTime"])
    months, days, years = zip(*[(d.month, d.day, d.year) for d in data_frame["dateTime"]])
    data_frame = data_frame.assign(month=months, day=days, year=years)
    data_frame = data_frame.drop("dateTime", axis=1)
    data_frame = data_frame.pivot(index=["month", "day"], columns="year", values="value")
    data_frame.index = data_frame.index.map(lambda t: f"{t[0]}/{t[1]}")
    data_frame[data_frame <= 0] = np.nan
    return data_frame


current_year = dt.date.today().year
# Only train forecast from data from the last x years.
# This *should* be a parameter that can be set by the user, but for now we'll hardcode it.
x_years_ago = current_year - 5

start_date = dt.date(x_years_ago, 1, 1)


def generate_prophet_forecast(
    site_id: str, reading_parameter: str, start_date: dt.date, end_date: dt.date
) -> pd.DataFrame:
    """Given a site, model, and length, returns a forecast DataFrame using fbprophet"""

    site_data = get_daily_average_data(
        site_id=site_id, reading_parameter=reading_parameter, start_date=start_date, end_date=end_date
    )
    clean_data = get_cleaned_data(site_data)
    clean_data.columns = ["ds", "y"]
    forecast_df = generate_forecast(clean_data)

    historic_df = clean_data[clean_data["ds"] >= dt.datetime(dt.date.today().year, 1, 1)]
    historic_df = historic_df.drop("ds", axis=1)
    historic_df.columns = ["past_value"]

    forecast_df.columns = ["forecast", "lower_error_bound", "upper_error_bound"]
    final_df = pd.concat([historic_df, forecast_df], ignore_index=True)

    today = dt.date.today()
    dates = pd.date_range(start=dt.date(today.year, 1, 1), end=dt.date(today.year, 12, 31))
    final_df.index = [date.strftime("%-m/%-d") for date in dates]  # add formatted dates

    return final_df


def get_cleaned_data(json_data: dict) -> pd.DataFrame:
    """Given usgs json data, cleans the data and returns a DataFrame"""

    data_frame = pd.DataFrame(json_data)
    data_frame = data_frame.drop("qualifiers", axis=1)
    data_frame["value"] = data_frame["value"].astype(float)
    data_frame["dateTime"] = pd.to_datetime(data_frame["dateTime"])
    data_frame.set_index("dateTime", inplace=True)
    data_frame = data_frame.asfreq("d")  # adds missing day data
    data_frame.loc[data_frame["value"] <= 0, "value"] = np.nan
    data_frame = data_frame.reset_index()
    data_frame = data_frame[["dateTime", "value"]]
    return data_frame


def generate_forecast(historic_data: pd.DataFrame) -> pd.DataFrame:
    """Takes in a training set (data - value) and a length to
    return a forecast DataFrame"""

    # historic_data = historic_data.ffill()  # Fill missing values for a better forecast
    # historic_data = historic_data.bfill()

    model = Prophet(interval_width=0.50)

    model.fit(historic_data)
    forecast = model.predict(
        model.make_future_dataframe(
            periods=get_forecast_length(historic_data.iloc[-1]["ds"].date()),
            include_history=False,
        )
    )
    forecast = forecast.round()

    return forecast[["yhat", "yhat_lower", "yhat_upper"]]


def get_forecast_length(last_data_day: dt.date) -> int:
    first_forecast_date = last_data_day + dt.timedelta(days=1)
    return pd.date_range(
        start=first_forecast_date, end=dt.date(first_forecast_date.year, 12, 31)
    ).size  # get number of remaining dates in the year including 'today'
