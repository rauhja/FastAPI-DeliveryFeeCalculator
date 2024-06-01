FROM --platform=linux/amd64 python:3.12.3-alpine AS builder

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base \
    && pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM --platform=linux/amd64 python:3.12.3-alpine

WORKDIR /app

COPY --from=builder /app/requirements.txt ./

RUN apk update && apk add --no-cache \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN addgroup -S appuser && adduser -S appuser -G appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
