""" Run before project generation """
import re
import sys


EMAIL_REGEX = r"^[a-z0-9]+[\._]?[a-z0-9]+@clearpeaks.com"
SLUG_REGEX = r"^[_a-z][_a-z0-9]+$"

email = "{{ cookiecutter.email }}"
project_slug = "{{ cookiecutter.project_slug }}"
create_makefile = "{{ cookiecutter.create_makefile }}"
create_dockerfile = "{{ cookiecutter.create_dockerfile }}"


def is_ok(key: str) -> bool:
    return key == "y" or key == "n"


# Check if it is a valid ClearPeaks email
if not re.match(EMAIL_REGEX, email):
    print(f"ERROR: {email} is not a valid ClearPeaks email! Should be *@clearpeaks.com")

    # exits with status 1 to indicate failure
    sys.exit(1)

# Check if it is a valid Python project slug name
if not re.match(SLUG_REGEX, project_slug):
    print(f"ERROR: {project_slug} is not a valid Python project slug name! \
        Must be lowercased, with underscores and/or numbers")

    # exits with status 1 to indicate failure
    sys.exit(1)

if not is_ok(create_makefile):
    print(f"ERROR: create_makefile expected 'y' or 'n', found {create_makefile}")

    # exits with status 1 to indicate failure
    sys.exit(1)

if not is_ok(create_dockerfile):
    print(f"ERROR: create_dockerfile expected 'y' or 'n', found {create_dockerfile}")

    # exits with status 1 to indicate failure
    sys.exit(1)
