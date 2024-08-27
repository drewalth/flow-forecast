import pandas as pd


def format_output(data: pd.DataFrame = None) -> dict:
    """Creates json dictionary with value label on value objects"""

    error_message = {"error": "No data found for this site"}

    body = error_message if data is None else data.reset_index().to_json(orient="records")

    return body
