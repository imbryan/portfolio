FROM node:24.5.0-alpine3.22 AS node-builder

WORKDIR /usr/src/app
COPY package.json package-lock.json ./

RUN npm install
COPY assets ./assets
COPY webpack.config.js .

RUN npm run dev

# FROM python:3.12-slim # CVE-2025-6020
FROM python:3.13.6-alpine3.21

# Security updates
# RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# alpine dependencies
RUN apk add --no-cache python3-dev py3-setuptools \
    musl-dev gcc cargo \
    tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY --from=node-builder /usr/src/app/static/js/bundles ./static/js/bundles