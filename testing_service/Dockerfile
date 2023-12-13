FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /testing-service

COPY ./requirements.txt /testing-service/
RUN pip install --no-cache-dir -r /testing-service/requirements.txt

COPY ./app /testing-service/app

EXPOSE 81

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port 81"]