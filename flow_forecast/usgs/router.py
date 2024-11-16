import datetime as dt
from typing import List

from fastapi import APIRouter, Query

from ..model.forecast_result import ForecastDataPoint
from ..utils import format_output
from .service import generate_prophet_forecast

usgs_router = APIRouter(
    prefix="/usgs",
    tags=["usgs"],
    responses={404: {"description": "Not found"}},
)


@usgs_router.get("/forecast")
async def forecast(
    site_id: str,
    reading_parameter: str = Query(default="00060"),
    start_date: dt.date = None,
    end_date: dt.date = None,
) -> List[ForecastDataPoint]:

    start_date = start_date if start_date else dt.date(dt.date.today().year, 1, 1)
    end_date = end_date if end_date else dt.date(dt.date.today().year, 12, 31)

    forecast_result = format_output(generate_prophet_forecast(site_id, reading_parameter, start_date, end_date))

    return forecast_result
