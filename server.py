import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config

from flow_forecast.main import app

config = Config()
config.bind = ["0.0.0.0:8000"]
asyncio.run(serve(app, config=config))
