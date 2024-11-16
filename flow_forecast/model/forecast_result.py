from typing import List

from pydantic import BaseModel, Field


class ForecastDataPoint(BaseModel):
    index: str = Field(description="The date or index of the data point.")
    past_value: float | None = Field(description="The past flow value for the given index.")
    forecast: float | None = Field(description="The forecasted flow value for the given index.")
    lower_error_bound: float | None = Field(description="The lower error bound of the forecast.")
    upper_error_bound: float | None = Field(description="The upper error bound of the forecast.")


class ForecastResult(BaseModel):
    data: List[ForecastDataPoint] = Field(description="The forecasted data points.")
