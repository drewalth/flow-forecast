# Description: Dockerfile for the flow_forecast service
# TODO: Slim down the image

FROM python

COPY pyproject.toml poetry.lock .

RUN pip install poetry && poetry install --only main --no-root --no-directory

COPY flow_forecast/ ./flow_forecast

RUN poetry install --only main

EXPOSE 5000

#  poetry run flask --app flow_forecast run

CMD ["poetry", "run", "flask", "--app", "flow_forecast", "run" , "--host=0.0.0.0"]