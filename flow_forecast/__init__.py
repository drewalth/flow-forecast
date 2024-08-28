import datetime
from flask import Flask
from flask import request
from flow_forecast.controllers import forecast_controller


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>flow-forecast</h1>"


@app.route("/forecast")
def forecast():
    default_start_date = datetime.date(1888, 1, 1)
    default_end_date = datetime.date(2100, 12, 31)
    default_reading_parameter = "00060"  # cubic feet per second (cfs)

    site_id = request.args.get("site_id")
    # if reading_parameter is not provided, default to "00060" (cfs)
    reading_parameter = (
        request.args.get("reading_parameter") if request.args.get("reading_parameter") else default_reading_parameter
    )

    #  if start_date or end_date are not provided, default to 1888-01-01 and 2100-12-31
    #  if they are provided, convert them to datetime.date objects

    start_date = request.args.get("start_date")

    if start_date:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    else:
        start_date = default_start_date

    end_date = request.args.get("end_date")

    if end_date:
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    else:
        end_date = default_end_date

    return forecast_controller.forecast(
        site_id=site_id, reading_parameter=reading_parameter, start_date=start_date, end_date=end_date
    )
