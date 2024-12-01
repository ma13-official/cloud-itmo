# Цель
Изучить так называемые "плохие практики" (антирекомендации) по написанию docker compose файлов и научиться их исправлять, чтобы получить верный грамотно составленный файл.

# Ход работы

## Плохой docker compose файл

Ниже представлен код плохого docker compose файла:

```yaml
version: "3"

services:
  app:
    image: python:3
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    environment:
      - ENV=development
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password

```

Чем он плох?

 1. Отсутствие конкретных версий образов: для python:3 и postgres не указаны версии, это может привести к проблемам, если в будущем версии базового образа изменятся.
 2. Хостовые каталоги монтируются в контейнер (volumes: - .:/app): это небезопасно (особенно на проде), так как позволяет изменить файлы на хосте.
 3. Отсутствие сети: по умолчанию сервисы будут работать в одной сети, это может стать проблемой, если необходимо изолировать их.
 4. Пароли передаются как открытый текст через environment.

## Хороший docker compose файл

Далее приведён код хорошего docker compose файла:

```yaml
version: "3.9"

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      ENV: production
    networks:
      - app_network
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "1.0"

  db:
    image: postgres:13.3
    environment:
      POSTGRES_USER_FILE: /run/secrets/db_user
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_user
      - db_password
    networks:
      - app_network

networks:
  app_network:
    driver: bridge

secrets:
  db_user:
    file: ./secrets/db_user.txt
  db_password:
    file: ./secrets/db_password.txt

```

Что исправлено?

 1. Указаны конкретные версии образов: python:3.9.7 и postgres:13.3.
 2. Удалено монтирование хостовых каталогов: вместо volumes используются заранее собранные образы..
 3. Добавлена сеть app_network для изоляции сервисов.
 4. Пароли вынесены в секреты Docker Compose (секреты подключаются через файл secrets).

## Настройка изоляции

Далее настроим изоляцию сервисов, чтобы контейнеры в рамках compose-проекта не "видели" друг друга по сети. А для этого нужно создать отдельные сети для каждого сервиса и не подключать их к общей сети.

```yaml
version: "3.9"

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      ENV: production
    networks:
      - app_network

  db:
    image: postgres:13.3
    environment:
      POSTGRES_USER_FILE: /run/secrets/db_user
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_user
      - db_password
    networks:
      - db_network

networks:
  app_network:
    driver: bridge
  db_network:
    driver: bridge

secrets:
  db_user:
    file: ./secrets/db_user.txt
  db_password:
    file: ./secrets/db_password.txt

```

## Вывод:
В ходе выполнения данной практической работы был создан "грамотный" Docker compose файл, а также создана основа для написания безопасных, удобных и масштабируемых конфигураций, это может быть полезным для организации контейнеризированных приложений.
