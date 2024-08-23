FROM python:3.11.4-alpine3.18
RUN addgroup flaskgroup && adduser -D flaskuser -G flaskgroup
WORKDIR /home/flaskuser/pythonserver
RUN apk update && pip install flask && pip install requests
COPY . .
RUN chown -R root:root /home/flaskuser/pythonserver
RUN chmod -R 555 /home/flaskuser/pythonserver
USER 1000:1000
EXPOSE 5000
ENTRYPOINT [ "python", "./src/flask.py" ]
