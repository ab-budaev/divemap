.DEFAULT_GOAL := help

.PHONY: help hooks up up-backend up-frontend down down-backend down-frontend

help: ## Показать доступные команды
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

hooks: ## Установить git-хуки (commit-msg: проверка conventional commits)
	pre-commit install --hook-type commit-msg

up: up-backend ## Поднять всё dev-окружение (бэкенд в фоне + фронтенд на переднем плане)
	$(MAKE) up-frontend

up-backend: ## Поднять только бэкенд (Docker Compose, в фоне)
	$(MAKE) -C backend up

up-frontend: ## Поднять только фронтенд (dev-сервер Vite)
	test -d frontend/node_modules || npm --prefix frontend install
	npm --prefix frontend run dev

down: down-frontend down-backend ## Остановить всё окружение (dev-сервер фронтенда + бэкенд)

down-backend: ## Остановить бэкенд
	$(MAKE) -C backend down

down-frontend: ## Остановить dev-сервер фронтенда
	-pkill -f "divemap/frontend.*vite"
