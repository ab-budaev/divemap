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
