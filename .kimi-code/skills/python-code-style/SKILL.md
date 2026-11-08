---
name: python-code-style
description: Python-стиль проекта. Использовать при любом написании или изменении Python-кода вместе со скиллом code-style. Также когда пользователь просит проверить Python-код на соответствие стилю.
---

# Python-стиль

Дополняет скилл `code-style`, который обязателен и имеет приоритет при противоречиях.

## Объекты-данные — pydantic

Любой объект, который просто несёт данные (DTO, доменные сущности, схемы запросов/ответов), — это `pydantic.BaseModel`. Не `dataclasses.dataclass`, не `NamedTuple`, не `TypedDict`, не голый `dict` на границах слоёв.

```python
import uuid

from pydantic import BaseModel, ConfigDict


class CurrentUserDTO(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: uuid.UUID
    name: str
```

- Неизменяемость — через `model_config = ConfigDict(frozen=True)`, а не `dataclass(frozen=True)`.
- `dataclasses` не импортируем вообще: если появился объект-данные — это pydantic.
- `Protocol` и ABC — не объекты-данные, к ним правило не относится.

## Тесты — pytest

### Тестовые данные — только фикстуры

Любой объект, который тест получает как данные (сущность, DTO, подготовленное значение), — это фикстура, подставляемая параметром теста. Никаких фабричных функций вида `make_user()` / `create_spot()` и вызовов их в теле теста.

Плохо:

```python
def make_user() -> User:
    return User(...)


def test_returns_current_user_dto() -> None:
    user = make_user()
```

Хорошо:

```python
@pytest.fixture
def user() -> User:
    return User(...)


def test_returns_current_user_dto(user: User) -> None:
```

- Нужен другой вариант объекта — отдельная фикстура с говорящим именем (`user_without_spots`), а не фабрика с аргументами.
- Фикстуры объявляются в `conftest.py`, не в тестовых модулях: общие для всего `tests/` — в корневом `tests/conftest.py`, для конкретного слоя — в `conftest.py` этого слоя (`tests/application/conftest.py`).
- Тестовые двойники (стабы, фейки) — это классы, а не фикстуры: класс живёт в обычном модуле (`tests/stubs.py`), а его экземпляры подставляются фикстурами (`user_repository`, `empty_user_repository`). Слой может переопределить общую фикстуру своей (например, с `dependency_overrides`) — стандартный fixture overriding pytest.
