FROM python:3.9

RUN mkdir -p /app
WORKDIR /app

RUN pip install "poetry==1.1.4"
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

ADD src /app/src

EXPOSE 8080

CMD gunicorn  --chdir src "fdk_baseregistries_publisher:create_app()"  --config=src/fdk_baseregistries_publisher/gunicorn_config.py
