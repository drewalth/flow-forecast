FROM python:3.12-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==$POETRY_VERSION"

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=${POETRY_CACHE_DIR} \
    poetry install --no-interaction --no-ansi --no-root --only main

FROM python:3.12-slim as runtime

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

COPY --from=builder /app/.venv /app/.venv

WORKDIR /app

COPY server.py .
COPY flow_forecast/ ./flow_forecast

EXPOSE 8000

ENTRYPOINT ["python", "-m", "server"]