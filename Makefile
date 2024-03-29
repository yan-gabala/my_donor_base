# !make_file

.PHONY: help

help: ## Покажет все доступные команды в make
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## Создаёт виртуальное окружение в папке venv
	python -m venv venv

install: ## Обновляет pip и устанавливает всё из requirements.txt
	python -m pip install --upgrade pip && \
	pip install -r requirements.txt
