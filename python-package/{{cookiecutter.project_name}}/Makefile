install:
    pip install -e .

install-dev:
    pip install -e . ".[dev]"

freeze:
    CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-index --output-file requirements.txt setup.py

lint:
    flake8 {{ cookiecutter.project_slug }}/ tests/

sort:
    isort {{ cookiecutter.project_slug }}/ tests/

format:
    black {{ cookiecutter.project_slug }}/ tests/

unit:
    pytest -sv tests/unit

coverage:
    coverage run --source={{ cookiecutter.project_slug }}/ --branch -m pytest tests/unit --junitxml=build/test.xml -v
    coverage xml -i -o build/coverage.xml
    coverage report

test: lint sort unit

run:
    python {{ cookiecutter.project_slug }}/

.PHONY: install install-dev lint sort format unit coverage test
