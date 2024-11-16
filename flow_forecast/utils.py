import json
from typing import List

import pandas as pd

from .model.forecast_result import ForecastDataPoint, ForecastResult


def format_output(data: pd.DataFrame = None) -> List[ForecastDataPoint]:
    """Creates list of ForecastDataPoint objects from a pandas DataFrame"""

    error_message = {"error": "No data found for this site"}

    body = error_message if data is None else data.reset_index().to_json(orient="records")

    result = ForecastResult(data=[])

    for item in json.loads(body):
        result.data.append(ForecastDataPoint(**item))

    return result.data
