# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

# Get started

There are several ways to build and run the project.\
The default Python execution start by installing the dependencies. To do so, run:

```sh
pip install -e .
```

This will install all the dependencies placed in `install_requires` variable in the [setup.py](setup.py) file. If you want to install the test dependencies, run:

```sh
pip install -e ".[dev]"
```

To run the project simply do:

```sh
python {{ cookiecutter.project_slug }}
```
{% if cookiecutter.create_makefile == "y" or cookiecutter.create_dockerfile == "y" %}
## Alternative running methods

As mentioned before, besides the regular Python execution, there are diverse ways to build and run this project.
{% endif %}
{% if cookiecutter.create_makefile == "y" %}
### Makefile

Special file containing shell commands. There are several commands you can run:

- make freeze: fill requirements.txt with the install requirements from the setup.py.
- make install: install requirements.txt.
- make lint: run flake8.
- make sort: run isort.
- make format: run black.
- make unit: run unit tests.
- make coverage: run code coverage.
- make test: run flake8, isort and unit tests.
- make run: run project.
{% endif %}
{% if cookiecutter.create_dockerfile == "y" %}
### Docker

First, make sure you have already generated the requirements.txt. With pip-compile or make freeze.\
Then, you have to build the docker image:

```sh
docker build -t {{ cookiecutter.project_slug }} .
```

Once built, you can run it using:

```sh
docker run {{ cookiecutter.project_slug }}
```

### Docker-compose

Run the following command to run the project using docker-compose:

```sh
docker-compose up
```
{% endif %}
## Test

The tests are placed in the `tests` folder. To run them, you can simply run:

```sh
pytest -sv tests/unit
```

## Code checkers

To assure the code quality we use various tools that check for guidelines and best practices.

### flake8

Simple tool that when executed outputs your code missing/error PEP8 guidelines. If there is no output, you are good to go!\
You can simply run `flake8 .` in the root folder.

### isort

Tool that automatically sorts your imports alphabetically. Clean and simple: `isort .` in the root folder.

### codecoverage

To check the coverage of your project, you first must have your code gathered in unit tests, and latter you can run these set of commands:

```sh
coverage run --source={{ cookiecutter.project_slug }}/ --branch -m pytest tests/unit --junitxml=build/test.xml -v
coverage xml -i -o build/coverage.xml
coverage report
```

This will display the % of code coverage of each file. You can find more information about coverage [here](https://coverage.readthedocs.io/en/coverage-5.5/).

### black

Powerful formatting tool that automatically formats your code following PEP8 guidelines.\
Be careful using this tool! Executing this tool can lead into undesired results.\
It is highly recommended to follow this steps:

1. Commit your code before executing.
2. Executing the command to a single file: `black {{ cookiecutter.project_slug }}/example.py`.
3. Adapting or reverting if necessary.
{% if cookiecutter.license != "none" %}
# License

Check [LICENSE](LICENSE).
{% endif %}
# Authors

This project has been developed by {{ cookiecutter.team }} team - ClearPeaks consultants:

- {{ cookiecutter.full_name }} | {{ cookiecutter.email }}

# About ClearPeaks

In ClearPeaks we are aware of the importance of delivering clean and readable code to our clients. Therefore, we develop our code under strict code guidelines and following the best practices to deliver quality products.

The guidelines we follow in Python are:

- Clean project structure.
- Inline code comments.
- Unit testing.
- README with necessary guidelines.
- PEP8 style guides.
- Codecoverage.
- Python Typing (for Python version>=3.5).

We assure its accomplishment by using tools such flake8, black and isort.

You can read more about us in our [website](https://www.clearpeaks.com/) were you will be able to see what [services](https://www.clearpeaks.com/bi-services/) we are offering, the [solutions](https://www.clearpeaks.com/bi-solutions-analytic-applications/) we are currently deliverying, and you will be able to read a vast of [blogs](https://www.clearpeaks.com/cp_blog/) where we discuss about many Big Data and BI topics and technologies. Furthermore, you can check our [GitHub](https://github.com/ClearPeaksSL) where we sometimes share with the community some interesting content.
