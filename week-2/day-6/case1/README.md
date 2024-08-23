# Django Web Uygulamasını Docker ile Ayağa Kaldırma

Bu proje, Django tabanlı bir web uygulamasını Docker konteyneri içerisinde çalıştırmak için gereken adımları içerir. Dockerfile'ı kullanarak bir Docker imajı oluşturacağız ve bu imajı kullanarak bir konteyner çalıştıracağız.

## Adımlar

### 1. Dockerfile Oluşturma

Proje dizininizde aşağıdaki içeriğe sahip bir `Dockerfile` oluşturun:

```dockerfile
# Dockerfile
FROM python:3.12.4-slim

RUN apt update && apt install iproute2 -y
WORKDIR /web-app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "webapp/manage.py", "runserver", "0.0.0.0:8000"]

### 2. Docker İmajını Oluşturma

Dockerfileın bulunduğu dizinde aşağıdaki komutu çalıştırarak Docker imajını oluşturun:

docker build -t django-app:1.0.0 .

Bu komut, django-app:1.0.0 adında bir Docker imajı oluşturacaktır.


### 3. Docker Konteynerini Çalıştırma

Oluşturduğunuz Docker imajını kullanarak bir konteyner çalıştırmak için aşağıdaki komutu kullanın:

docker run --name django-container -p 8000:8000 django-app:1.0.0

Bu komut, django-container adında bir Docker konteyneri oluşturacak ve 8000 portunu yerel makinenizde kullanılabilir hale getirecektir.


### 4. Docker İmajını Docker Hub'a Pushlama

-docker login
-docker tag django-app:1.0.0 yourusername/django-app:1.0.0
-docker push yourusername/django-app:1.0.0

