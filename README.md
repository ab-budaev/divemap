# Карта погружений (divemap)

Персональный дайвлог с интерактивной картой мест погружений: добавляйте места кликом по карте, ведите журнал погружений и прикрепляйте фото.

## Стек

- **Backend** (`backend/`): Python 3.14, FastAPI, SQLAlchemy 2.0, Alembic, pydantic-settings
- **БД**: PostgreSQL (Docker Compose, локальный каталог данных `.data/pgdata` на хосте)

## Требования

- Docker и Docker Compose
- [uv](https://docs.astral.sh/uv/) — для локальной разработки backend-кода вне контейнера (опционально)

## Локальный запуск

1. Скопируй `.env.example` в `.env` внутри `backend/` и поправь под себя:

   ```sh
   cp backend/.env.example backend/.env
   ```

2. Подними окружение одной командой (соберёт и запустит сервисы приложения и базы):

   ```sh
   make -C backend up
   ```

3. Проверь, что сервис отвечает:

   ```sh
   curl http://localhost:8000/health   # {"status":"ok"}
   ```

Данные PostgreSQL хранятся в локальном каталоге `backend/.data/pgdata` на хосте (bind mount) и переживают перезапуск и пересоздание контейнеров.

## Структура репозитория

```text
backend/              # Python-бэкенд (FastAPI)
  src/
    api/              # presentation: FastAPI-приложение и роутеры
    application/      # сценарии использования (use cases)
    domain/           # бизнес-сущности и правила
    infrastructure/   # хранение данных: SQLAlchemy engine/session
  migrations/         # миграции Alembic
  tests/              # pytest-тесты
  compose.yml         # сервисы app и db (PostgreSQL)
  Dockerfile
  Makefile
  .env.example
openspec/             # спецификации продукта (OpenSpec)
```

## Разработка backend

Установка зависимостей, команды линтера, тестов и локального запуска — см. [backend/README.md](backend/README.md).

## Статус

В разработке. Реализован фундамент backend-сервиса и локальное окружение разработки. Этапы интерактивной карты, мест и журнала погружений — впереди.
