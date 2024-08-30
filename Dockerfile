# Description: Dockerfile for the flow_forecast service
# TODO: Slim down the image

FROM python

COPY pyproject.toml poetry.lock .

RUN pip install poetry && poetry install --only main --no-root --no-directory

COPY flow_forecast/ ./flow_forecast

RUN poetry install --only main

EXPOSE 3000

CMD ["poetry", "run", "waitress-serve", "--host", "0.0.0.0", "--port" , "3000", "flow_forecast:app"]