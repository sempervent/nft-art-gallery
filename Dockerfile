FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

CMD ["poetry", "run", "python", "app/main.py"]
