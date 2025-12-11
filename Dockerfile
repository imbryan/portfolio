FROM node:25.2.1-alpine3.23 AS node-builder

WORKDIR /usr/src/app
COPY package.json package-lock.json ./

RUN ["/bin/sh", "-c", "npm install"]
COPY assets ./assets
COPY webpack.config.js .

RUN ["/bin/sh", "-c", "npm run dev"]

FROM python:3.14.2-alpine3.23

# Security updates
# RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN ["/bin/sh", "-c", "apk update && apk upgrade && rm -rf /var/cache/apk/*"]

# alpine dependencies
RUN ["/bin/sh", "-c", "apk add --no-cache python3-dev py3-setuptools \
    musl-dev gcc cargo \
    tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev"]

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN ["/bin/sh", "-c", "pip install --upgrade pip"]
COPY ./requirements.txt .
RUN ["/bin/sh", "-c", "pip install -r requirements.txt"]

COPY . .
COPY --from=node-builder /usr/src/app/static/js/bundles ./static/js/bundles
