# Карта погружений (divemap)

Персональный дайвлог с интерактивной картой мест погружений: добавляйте места кликом по карте, ведите журнал погружений и прикрепляйте фото.

## Стек

- **Frontend** (`frontend/`): React 19, TypeScript, Vite, TanStack Query; production-сборка — отдельный Docker-образ (nginx + статика)
- **Backend** (`backend/`): Python 3.14, FastAPI, SQLAlchemy 2.0, Alembic, pydantic-settings
- **БД**: PostgreSQL (Docker Compose, локальный каталог данных `.data/pgdata` на хосте)

## Требования

- Docker и Docker Compose
- Node.js 24+ и npm — для разработки фронтенда
- [uv](https://docs.astral.sh/uv/) — для локальной разработки backend-кода вне контейнера (опционально)

## Локальный запуск

1. Скопируй `.env.example` в `.env` внутри `backend/` и поправь под себя:

   ```sh
   cp backend/.env.example backend/.env
   ```

2. Настрой ключ Яндекс.Карт для фронтенда:

   ```sh
   cp frontend/.env.example frontend/.env
   ```

   Получи ключ в [кабинете разработчика Яндекса](https://developer.tech.yandex.ru/): «Подключить API» → сервис «JavaScript API», бесплатный тариф. В настройках ключа укажи домен `localhost`. Впиши ключ в `frontend/.env`:

   ```
   VITE_YANDEX_MAPS_API_KEY=твой_ключ
   ```

   Без ключа приложение запустится, но вместо карты покажет сообщение об ошибке конфигурации.

3. Подними всё окружение одной командой из корня репозитория:

   ```sh
   make up
   ```

   Команда поднимает бэкенд (приложение + PostgreSQL в Docker Compose, в фоне), при необходимости устанавливает npm-зависимости и запускает dev-сервер фронтенда на переднем плане.

4. Открой http://localhost:5173 — главный экран покажет интерактивную Яндекс.Карту с демо-маркерами мест.

Полезные команды:

```sh
make up-backend     # только бэкенд (API на :8000)
make up-frontend    # только dev-сервер фронтенда (:5173)
make down           # остановить всё окружение (и фронтенд, и бэкенд)
```

Данные PostgreSQL хранятся в локальном каталоге `backend/.data/pgdata` на хосте (bind mount) и переживают перезапуск и пересоздание контейнеров.

## Структура репозитория

```text
frontend/             # SPA-фронтенд (React + TypeScript, Vite)
  src/
    api/              # слой доступа к API: fetch-клиент и endpoint-функции
    components/       # переиспользуемые UI-компоненты
    features/         # функциональные модули (map — интерактивная Яндекс.Карта)
    styles/           # глобальные стили
  Dockerfile          # отдельный образ фронтенда (nginx + статика)
  nginx.conf
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

## Разработка frontend

```sh
cd frontend
npm install         # первый раз
npm run dev         # dev-сервер с hot-reload на :5173, /api проксируется на :8000
npm run build       # production-сборка в dist/
npm run lint        # oxlint
npx tsc -b --noEmit # проверка типов
```

Production-образ фронтенда собирается отдельно от бэкенда:

```sh
docker build --build-arg VITE_YANDEX_MAPS_API_KEY=твой_ключ -t divemap-frontend frontend/
docker run --rm -p 8080:80 divemap-frontend   # статика на :8080
```

Ключ Яндекс.Карт подставляется в сборку на этапе `docker build` (Vite вшивает `import.meta.env` в статику), в сам образ и репозиторий он не попадает.

## Разработка backend

Установка зависимостей, команды линтера, тестов и локального запуска — см. [backend/README.md](backend/README.md).

## Статус

В разработке. Реализованы фундамент backend-сервиса, локальное окружение разработки и главный экран с интерактивной Яндекс.Картой (демо-маркеры, панели места и создания места). Этапы мест и журнала погружений — впереди.
