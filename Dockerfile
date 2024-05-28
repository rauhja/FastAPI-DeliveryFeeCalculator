FROM --platform=linux/amd64 python:3.11

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY app ./app

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-dev

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
