# case2


services:
  django-app:
    image: django-app:1.0.0
    container_name: django-app-1-0-0
    ports:
      - 2222:8000
    restart: always
    networks:
      my-network:
        ipv4_address: 192.168.1.120


networks:
  my-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 192.168.1.0/24
          gateway: 192.168.1.1


bu işlemlerden sonra;

docker compose up komutu ile bu docker compose yaml dosyasını çalıştırıyoruz.
kontrol etmek için 
docker ps'e bakabilir veya localhost:2222 adresini tarayıcımızda aratabiliriz.