FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev
COPY . /app
CMD ["poetry", "run", "python", "app/main.py"]
