# Dockerfile
FROM python:3.12.4-slim

RUN apt update && apt install iproute2 -y
WORKDIR /web-app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "webapp/manage.py", "runserver", "0.0.0.0:8000"]



