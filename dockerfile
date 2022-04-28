FROM python:3.10

MAINTAINER "pygopher@yahoo.com"

WORKDIR /app/

COPY ./requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app/

CMD ["uvicorn", "main.main:app", "--host", "0.0.0.0", "--port", "80"]
