# import pandas as pd
# import json
# from ..model.forecast_result import ForecastResult, ForecastDataPoint
# def format_output(data: pd.DataFrame = None) -> ForecastResult:
#     """Creates json dictionary with value label on value objects"""

#     error_message = {"error": "No data found for this site"}

#     body = error_message if data is None else data.reset_index().to_json(orient="records")

#     result = ForecastResult(data=[])

#     for item in json.loads(body):
#         result.data.append(ForecastDataPoint(**item))

#     return result
