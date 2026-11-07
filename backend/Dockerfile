FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS base

ENV APPROOT=/opt/divemap-backend
ENV PYTHONPATH=${APPROOT}/src
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy

FROM base AS dev

RUN apt-get update && \
    apt-get install --assume-yes --no-install-recommends \
    make \
    git \
    bash-completion && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APPROOT}

COPY pyproject.toml uv.lock ./
RUN uv sync --all-groups

COPY src ./src
COPY alembic.ini entrypoint.sh ./
COPY migrations ./migrations
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

FROM base AS builder

WORKDIR ${APPROOT}

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

FROM base AS release

ENV USERNAME=app
ENV USER_UID=1000
ENV USER_GID=${USER_UID}

RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

WORKDIR ${APPROOT}

COPY --from=builder ${APPROOT}/.venv ${APPROOT}/.venv

COPY src ./src
COPY alembic.ini entrypoint.sh ./
COPY migrations ./migrations
RUN chmod +x ./entrypoint.sh

EXPOSE 8000

USER ${USERNAME}

ENTRYPOINT ["./entrypoint.sh"]
