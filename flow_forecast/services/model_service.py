import datetime as dt

import pandas as pd

from flow_forecast.models.prophet_forecast import generate_forecast

# from app.models import fbprophet as fbp
# from app.models import holt_winters as hwes
from flow_forecast.services import usgs_service

# try:
#     import unzip_requirements  # noqa: F401
# except ImportError:
#     pass

start_date = dt.date(1990, 1, 1)  # only train forecast from data since 1990


# def generate_holt_winters_forecast(site_id: str, forecast_length: int) -> pd.DataFrame:  # noqa: E501
#     """Given a site, model, and length, returns a forecast DataFrame"""

#     site_data = usgs_service.get_daily_average_data(site_id, start_date)
#     clean_data = usgs_service.clean_data(site_data)
#     offset_days = int((dt.datetime.today() - clean_data.tail(1).index).days[0])
#     offset_days += int(forecast_length)

#     fitted_model = hwes.ets_fit_model(clean_data["value"].tolist())
#     forecast_list = fitted_model.forecast(offset_days)
#     forecast_dates = pd.date_range(
#         clean_data.tail(1).index[0] + dt.timedelta(days=1),
#         periods=offset_days,
#     )
#     formatted_dates = [date.strftime("%m/%d") for date in forecast_dates]

#     return pd.DataFrame({"forecast": forecast_list}, index=formatted_dates)


def generate_prophet_forecast(site_id: str) -> pd.DataFrame:
    """Given a site, model, and length, returns a forecast DataFrame using fbprophet"""

    site_data = usgs_service.get_daily_average_data(site_id)
    clean_data = usgs_service.clean_data(site_data)
    clean_data.columns = ["ds", "y"]
    forecast_df = generate_forecast(clean_data)

    historic_df = clean_data[
        clean_data["ds"] >= dt.datetime(dt.date.today().year, 1, 1)
    ]
    historic_df = historic_df.drop("ds", axis=1)
    historic_df.columns = ["past_value"]

    forecast_df.columns = ["forecast", "lower_error_bound", "upper_error_bound"]
    final_df = pd.concat([historic_df, forecast_df], ignore_index=True)

    today = dt.date.today()
    dates = pd.date_range(
        start=dt.date(today.year, 1, 1), end=dt.date(today.year, 12, 31)
    )
    final_df.index = [date.strftime("%-m/%-d") for date in dates]  # add formatted dates

    return final_df