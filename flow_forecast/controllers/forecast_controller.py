import datetime
from flow_forecast.services import model_service
from flow_forecast.helpers import controller_helper


def forecast(site_id: str, reading_parameter: str, start_date: datetime.date, end_date: datetime.date) -> dict:
    forecast = model_service.generate_prophet_forecast(site_id, reading_parameter, start_date, end_date)
    return controller_helper.format_output(forecast)
