# !make_test

venv: ## Make a new virtual environment
	python -m venv venv

install: ## Make install requirements
	python -m pip install --upgrade pip && \
	pip install -r requirements-dev.txt
