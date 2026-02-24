## NODE BUILDER ##
FROM node:25.6-slim AS node-builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY assets ./assets
COPY webpack.config.js .
RUN npm run build

## PYTHON BUILDER ##
FROM python:3.14-slim AS python-builder
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:0.10.4 /uv /uvx /bin/
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

## DEVELOPMENT STAGE ##
FROM python-builder AS development
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --group dev
COPY . .
ENV PATH="/app/.venv/bin:$PATH"

## PRODUCTION STAGE ##
FROM python-builder AS production
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
RUN groupadd -g 1001 app && \
    useradd -u 1001 -g app -s /bin/sh -m app
WORKDIR /app
RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --no-dev
COPY --from=node-builder /app/static/js/bundles ./static/js/bundles
COPY . .
RUN chown -R app:app /app
USER app
ENV PATH="/app/.venv/bin:$PATH"
