# import datetime as dt
# import logging

# import pandas as pd
# from prophet import Prophet


# def generate_forecast(historic_data: pd.DataFrame) -> pd.DataFrame:
#     """Takes in a training set (data - value) and a length to
#     return a forecast DataFrame"""

#     # historic_data = historic_data.ffill()  # Fill missing values for a better forecast
#     # historic_data = historic_data.bfill()
#     logging.getLogger("prophet").setLevel(logging.WARNING)
#     model = Prophet(interval_width=0.50)

#     model.fit(historic_data)
#     forecast = model.predict(
#         model.make_future_dataframe(
#             periods=get_forecast_length(historic_data.iloc[-1]["ds"].date()),
#             include_history=False,
#         )
#     )
#     forecast = forecast.round()

#     return forecast[["yhat", "yhat_lower", "yhat_upper"]]


# def get_forecast_length(last_data_day: dt.date) -> int:
#     first_forecast_date = last_data_day + dt.timedelta(days=1)
#     return pd.date_range(
#         start=first_forecast_date, end=dt.date(first_forecast_date.year, 12, 31)
#     ).size  # get number of remaining dates in the year including 'today'
