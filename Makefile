.PHONY: hooks

# Установить git-хуки (commit-msg: проверка conventional commits)
hooks:
	pre-commit install --hook-type commit-msg
