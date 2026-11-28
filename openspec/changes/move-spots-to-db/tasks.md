# Tasks

[[_TOC_]]

## 1. Backend: модель и миграция

- [x] 1.1 [Backend] Создать миграцию Alembic с таблицей `spots` (id UUID PK, name Text NOT NULL, description Text NULL, lat/lng Double NOT NULL, created_at/updated_at DateTime(tz) с server default `now()`) и сидами трёх демо-точек из `frontend/src/features/map/spots.ts` с фиксированными UUID; `downgrade` удаляет таблицу. Критерий приёмки: после `alembic upgrade head` таблица создана и содержит 3 строки с корректными данными; после `alembic downgrade -1` таблица удалена.
- [x] 1.2 [Backend] Создать доменную сущность `Spot` (frozen pydantic) и протокол `SpotRepository` в `backend/src/domain/spots.py` по образцу `domain/users.py`. Критерий приёмки: `make lint` проходит, модуль импортируется.

## 2. Backend: слои и API

- [x] 2.1 [Backend] Создать `SpotModel` и `SqlAlchemySpotRepository` в `backend/src/infrastructure/spots.py` по образцу `infrastructure/users.py` (метод получения всех спотов, сортировка по `created_at`). Критерий приёмки: репозиторий возвращает споты из тестовой/локальной БД, `make lint` проходит.
- [x] 2.2 [Backend] Создать `SpotDTO` и use-case `ListSpots` в `backend/src/application/spots.py` по образцу `application/users.py`. Критерий приёмки: `make lint` проходит.
- [x] 2.3 [Backend] Создать роутер `GET /spots` в `backend/src/api/routers/spots.py` со схемой ответа (id, name, description nullable, lat, lng), зарегистрировать его в `api/app.py` и добавить провайдер `get_spot_repository` в `api/dependencies.py`. Критерий приёмки: запущенный backend отвечает на `GET /spots` кодом 200 и массивом из 3 демо-спотов с корректными полями; `make test` и `make lint` проходят.

## 3. Frontend: загрузка спотов через API

- [x] 3.1 [Frontend] Создать модуль `frontend/src/api/spots.ts` с типом `Spot` (id: string, name, description nullable, lat, lng) и функцией запроса списка на базе `apiFetch` из `api/client.ts`. Критерий приёмки: тип соответствует контракту `GET /spots`, линт фронтенда проходит.
- [x] 3.2 [Frontend] Перевести `MapScreen` на загрузку спотов через API при монтировании: состояния загрузки, ошибки (сообщение + кнопка «Повторить») и успеха; маркеры строятся из ответа API, конвертация `lat`/`lng` → `[lng, lat]` для Яндекс.Карт в одном месте; `SpotPanel` работает с новым типом `Spot`. Критерий приёмки: при запущенном backend карта показывает 3 маркера в тех же местах, клик по маркеру открывает карточку с названием и описанием; при остановленном backend видно сообщение об ошибке, кнопка «Повторить» перезапрашивает данные.
- [x] 3.3 [Frontend] Удалить хардкод: файл `frontend/src/features/map/spots.ts` и все импорты `demoSpots`/`DemoSpot`. Критерий приёмки: поиск по `demoSpots`/`DemoSpot` в `frontend/src` не находит совпадений, сборка и линт фронтенда проходят.

## 4. Проверка end-to-end

- [x] 4.1 [Infra] Прогнать полный цикл: поднять docker-compose (db + backend), применить миграции, проверить карту в браузере — маркеры из БД, данные переживают перезагрузку страницы и рестарт backend. Критерий приёмки: сценарии спецификации `map-spots` воспроизводятся вручную; `make lint` и `make test` зелёные в обоих пакетах.
