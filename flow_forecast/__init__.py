from flask import Flask
from flask import request
from flow_forecast.controllers import forecast_controller

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>flow-forecast</h1>"

@app.route("/forecast")
def forecast():
    site_id = request.args.get('site_id')
    return forecast_controller.forecast(site_id=site_id)