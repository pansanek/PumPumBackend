FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /task-service

COPY ./requirements.txt /task-service/
RUN pip install --no-cache-dir -r /task-service/requirements.txt

COPY ./app /task-service/app
COPY ./migration /task-service/migration
COPY ./alembic.ini /task-service/alembic.ini


EXPOSE 80

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port 80"]
