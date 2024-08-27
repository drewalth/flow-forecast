from flow_forecast.services import model_service
from flow_forecast.helpers import controller_helper

def forecast(site_id: str):
    forecast = model_service.generate_prophet_forecast(site_id)
    return controller_helper.format_output(forecast)