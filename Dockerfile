# Description: Dockerfile for the flow_forecast service
# TODO: Slim down the image

# FROM python

# COPY pyproject.toml poetry.lock .

# RUN pip install poetry && poetry install --only main --no-root --no-directory

# COPY server.py .
# COPY flow_forecast/ ./flow_forecast

# RUN poetry install --only main

# EXPOSE 8000

# ENTRYPOINT ["python", "-m", "server"]


FROM python:3.12 as builder

RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR='/tmp/poetry_cache'

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=${POETRY_CACHE_DIR} \
    poetry install --without dev --no-root


FROM python:3.12 as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY server.py .
COPY flow_forecast/ ./flow_forecast

ENTRYPOINT ["python", "-m", "server"]