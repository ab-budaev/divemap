# Tasks

[[_TOC_]]

## 1. Backend: домен и application-слой

- [x] 1.1 [Backend] Расширить протокол `SpotRepository` в `backend/src/domain/spots.py` методом `create(name, description, lat, lng) -> Spot`. Критерий приёмки: протокол объявляет метод создания; `make -C backend mypy` проходит.
- [x] 1.2 [Backend] Добавить use-case `CreateSpot` в `backend/src/application/spots.py` по образцу `ListSpots`: принимает репозиторий и входные данные, возвращает `SpotDTO`. Критерий приёмки: use-case делегирует создание репозиторию и возвращает DTO созданного спота.
- [x] 1.3 [Backend] Реализовать `create` в `SqlAlchemySpotRepository` (`backend/src/infrastructure/spots.py`): `add` + `commit` + `refresh`, возврат доменного объекта через `to_domain()`. Критерий приёмки: запись сохраняется в таблицу `spots`, возвращаемый объект содержит серверные значения (`id`, `created_at`).
- [x] 1.4 [Backend] Дополнить `tests/application/test_spots.py` тестом use-case `CreateSpot` на стаб-репозитории. Критерий приёмки: `make -C backend test` зелёный, тест проверяет, что данные доходят до репозитория и возвращается DTO.

## 2. Backend: эндпоинт POST /spots

- [x] 2.1 [Backend] Добавить в `backend/src/api/routers/spots.py` модель запроса `SpotCreateRequest` (pydantic: `name` — обязателен, непустой после trim; `description` — опционально; `lat` ∈ −90..90; `lng` ∈ −180..180 через `Field`) и эндпоинт `POST /spots` со статусом 201 и `response_model=SpotResponse`. Критерий приёмки: OpenAPI (`/docs`) показывает `POST /spots` с телом запроса и ответом 201.
- [x] 2.2 [Backend] Дополнить `tests/api/test_spots.py`: успешное создание (201, тело ответа, запись видна в `GET /spots`), создание без описания, 422 на пустое/пробельное `name`, 422 на координаты вне диапазона. Критерий приёмки: `make -C backend test` зелёный.
- [x] 2.3 [Backend] Прогнать `make -C backend lint` и `make -C backend test`. Критерий приёмки: оба прогона зелёные.

## 3. Frontend: интеграция модалки с API

- [x] 3.1 [Frontend] Расширить `apiFetch` в `frontend/src/api/client.ts` поддержкой метода и тела запроса (POST + JSON). Критерий приёмки: существующие GET-вызовы работают без изменений, TypeScript-сборка проходит.
- [x] 3.2 [Frontend] Добавить `createSpot` в `frontend/src/api/spots.ts`: `POST /spots` с `{name, description, lat, lng}`, возвращает созданный `Spot`. Критерий приёмки: функция типизирована, возвращает `Promise<Spot>`.
- [x] 3.3 [Frontend] В `frontend/src/features/map/MapScreen.tsx` заменить обработчик-заглушку на `useMutation(createSpot)` с инвалидацией `['spots']` в `onSuccess`; закрытие модалки — только после успеха. Критерий приёмки: после сохранения список перезапрашивается, новый маркер появляется на карте без перезагрузки страницы.
- [x] 3.4 [Frontend] В `frontend/src/features/map/CreateSpotModal.tsx` добавить состояния отправки и ошибки: кнопка «Сохранить» заблокирована во время запроса, при ошибке окно остаётся открытым с введёнными данными и показывает сообщение об ошибке. Критерий приёмки: при недоступном API форма не закрывается, введённые значения на месте, отображается сообщение; повторная отправка во время запроса невозможна.
- [x] 3.5 [Frontend] Прогнать линтер и сборку фронтенда (согласно командам проекта). Критерий приёмки: прогон зелёный.

## 4. Сквозная проверка

- [x] 4.1 [Infra] Поднять окружение (`make up`), создать место через UI кликом по карте, убедиться, что маркер появился. Критерий приёмки: сценарий «клик → форма → сохранить → маркер на карте» работает end-to-end.
- [x] 4.2 [Infra] Перезагрузить страницу и рестартовать бэкенд (`make down && make up-backend`). Критерий приёмки: созданное место отображается на карте — данные персистятся в PostgreSQL.
