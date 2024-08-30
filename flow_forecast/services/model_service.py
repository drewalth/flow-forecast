import datetime as dt
import pandas as pd
from flow_forecast.models.prophet_forecast import generate_forecast
from flow_forecast.services import usgs_service


current_year = dt.date.today().year
# Only train forecast from data from the last x years.
# This *should* be a parameter that can be set by the user, but for now we'll hardcode it.
x_years_ago = current_year - 5

start_date = dt.date(x_years_ago, 1, 1)


def generate_prophet_forecast(site_id: str, reading_parameter: str, start_date: dt.date, end_date: dt.date) -> pd.DataFrame:
    """Given a site, model, and length, returns a forecast DataFrame using fbprophet"""

    site_data = usgs_service.get_daily_average_data(
        site_id=site_id, reading_parameter=reading_parameter, start_date=start_date, end_date=end_date
    )
    clean_data = usgs_service.clean_data(site_data)
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
