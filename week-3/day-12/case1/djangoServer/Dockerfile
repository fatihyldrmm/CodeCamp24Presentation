FROM python:3.11.4-alpine3.18
RUN addgroup djangogroup && adduser -D djangouser -G djangogroup
WORKDIR /home/djangouser/pythonserver
RUN apk update && pip install django && pip install requests
COPY . .
RUN chown -R root:root /home/djangouser/pythonserver
RUN chmod -R 555 /home/djangouser/pythonserver
USER 1000:1000
EXPOSE 5000
ENTRYPOINT [ "python", "./djangoServer/manage.py" ]
