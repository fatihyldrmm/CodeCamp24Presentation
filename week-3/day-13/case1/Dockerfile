# Python imajını temel al
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /home/djangouser/pythonserver

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt /home/djangouser/pythonserver/
RUN pip install --no-cache-dir -r requirements.txt

# Django uygulamasını kopyala
COPY . /home/djangouser/pythonserver/

# Ortam değişkenini ayarla
ENV DJANGO_SETTINGS_MODULE=djangoServer.settings

# Portu aç
EXPOSE 8085

# Django uygulamasını çalıştır
CMD ["python", "./djangoServer/manage.py", "runserver", "0.0.0.0:8085"]
