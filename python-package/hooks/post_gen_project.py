""" Run after project generation """
import os
import shutil


def remove(filepath: str) -> None:
    if os.path.isfile(filepath):
        os.remove(filepath)
        print(f"Removed {filepath}")
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)
        print(f"Removed {filepath}")


create_makefile = "{{cookiecutter.create_makefile}}" == "y"
create_dockerfile = "{{cookiecutter.create_dockerfile}}" == "y"
create_license = "{{cookiecutter.license}}" != "none"

if not create_makefile:
    remove("Makefile")

if not create_dockerfile:
    remove("Dockerfile")
    remove("docker-compose.yml")

if not create_license:
    remove("LICENSE")

message = """
The project has been successfully installed!\n\n
Remember checking the CODING_GUIDELINES in https://github.com/ClearPeaksSL/clearpeaks-programming-guidelines/CONTRIBUTING.md and to \
upload your project to a GitHub repository!\n
Contact Maintainers for help if needed.
"""

print(message)
