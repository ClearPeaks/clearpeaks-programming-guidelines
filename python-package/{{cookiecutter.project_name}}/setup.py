#!/usr/bin/env python

import os
import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.md").read()

install_requires = []

dev_requires = [
    "flake8>=3.9.2",
    "flake8-annotations>=2.6.2"
    "black>=21.7b0",
    "isort>=5.9.3",
    "pytest>=6.2.4",
    "pytest-mock>=3.6.1",
    "coverage>=5.5",
    "pip-tools>=6.2.0"
]

setup(
    name="clearpeaks-{{ cookiecutter.project_slug }}",
    version="1.0.0",
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/ClearPeaksSL/{{ cookiecutter.project_slug }}",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=["pytest"],
    tests_require=dev_requires,
    extras_require={
        "dev": dev_requires
    },
    {%- if cookiecutter.license == "MIT" %}
    license="MIT",
    {%- elif cookiecutter.license == "Apache Software License 2.0" %}
    license="Apache2",
    {%- elif cookiecutter.license == "GNU GPL v3.0" %}
    license="GPLv3",
    {% endif %}
    zip_safe=False,
    keywords="{{ cookiecutter.project_name }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        {%- if cookiecutter.license == "MIT" %}
        "License :: OSI Approved :: MIT License",
        {%- elif cookiecutter.license == "Apache Software License 2.0" %}
        "License :: OSI Approved :: Apache Software License",
        {%- elif cookiecutter.license == "GNU GPL v3.0" %}
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        {% endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ]
)
