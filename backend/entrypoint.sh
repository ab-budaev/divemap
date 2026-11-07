#!/bin/bash
set -euo pipefail

cd /opt/divemap-backend
export PYTHONPATH=/opt/divemap-backend/src

DB_RETRIES="${DB_RETRIES:-30}"
DB_SLEEP="${DB_SLEEP:-2}"

# Ждём готовности базы данных и применяем миграции Alembic перед стартом сервера.
for i in $(seq 1 "${DB_RETRIES}"); do
  if .venv/bin/alembic upgrade head; then
    break
  fi
  if [ "${i}" -eq "${DB_RETRIES}" ]; then
    echo "Database is not reachable after ${DB_RETRIES} attempts" >&2
    exit 1
  fi
  echo "Waiting for database (attempt ${i}/${DB_RETRIES})..."
  sleep "${DB_SLEEP}"
done

exec .venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 "$@"
