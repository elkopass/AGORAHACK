# AGORAHACK

Сервис для аккумуляции данных между ERP системами

## Архитектура решения

- **marketplace** - основной бекенд на Django
- **gateway** - микросервис для приема и конвертации данных от ERP
- **rabbitmq** - брокер сообщений между gateway и marketplace
- **postgresql** - персистентное хранилище данных

## Сборка и развертывание

### С использованием Docker

1. Создаем файл `.env` в корневой директории следующего содержания:

```
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>

PG_DATA=/data/postgres

RABBITMQ_USERNAME=<your_rabbit_user>
RABBITMQ_PASSWORD=<your_rabbit_password>

RABBITMQ_NODE_PORT_NUMBER=56721
RABBITMQ_REMOTE_HOST=agora_rabbitmq
```

2. Поднимаем все сервисы командой ` $ sudo docker-compose up --build -d`

### Из исходников

Инструкции для запуска отдельных сервисов лежат в их поддиректориях

## Стенды

### Наш тестовый стенд

TODO

### Локальный стенд

Если вы запустили всё в докере локально, то

- Сервис gateway работает по адресу http://localhost:5001
- Cервис marketplace работает по адресу http://localhost:8001


## Обратная связь


![meme](https://github.com/elkopass/AGORAHACK/img/meme.jpeg)
