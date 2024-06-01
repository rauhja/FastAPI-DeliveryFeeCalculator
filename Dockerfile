FROM --platform=linux/amd64 python:3.12.0-alpine AS builder

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base \
    && pip install --no-cache-dir poetry

COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev

FROM --platform=linux/amd64 python:3.12.0-alpine

WORKDIR /app

COPY --from=builder /app /app

RUN addgroup -S appuser && adduser -S appuser -G appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["sh", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
