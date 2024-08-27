import pandas as pd


def format_output(
    data: pd.DataFrame = None
) -> dict:
    """Creates json dictionary with value label on value objects"""

    body = (
        error_message if data is None else data.reset_index().to_json(orient="records")
    )

    return body