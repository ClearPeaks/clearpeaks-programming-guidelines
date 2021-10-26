![ClearPeaks Logo](https://www.clearpeaks.com/wp-content/uploads/2017/08/Clearpeaks-logo_smaller-1.svg)

# ClearPeaks Programming Guidelines

In ClearPeaks we are continuously deliverying code to our clients, thereby, like in our BI projects, we must deliver quality results. Therefore, we have developed this repository with the [coding guidelines](CODING_GUIDELINES.md) we encourage our consultants to follow, along with some generic project templates that will fasten the project creation following project structure guidelines.

In this repository, we only have the most generic project templates. You can find team-specific templates in the following repositories:

| Team | Repository |
| ---- | ----- |
| Big Data and Cloud | [big-data-project-templates](https://github.com/ClearPeaksSL/big-data-project-templates) |
| Advanced Analytics | [advanced-analytics-project-templates](https://github.com/ClearPeaksSL/advanced-analytics-project-templates) |
| Web and mobile | [web-mobile-project-templates](https://github.com/ClearPeaksSL/web-mobile-project-templates) |
| Oracle | [oracle-project-templates](https://github.com/ClearPeaksSL/oracle-project-templates) |
| Modern BI | [modern-bi-project-templates](https://github.com/ClearPeaksSL/modern-bi-project-templates) |

## ✨ Get started

Every template project has a README explaining all the content in it and its purpose (why X folder is needed and what to store in it, styling tools...), so any consultant can understand what they are downloading.

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a tool that leverages [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templates and can be installed in your computer using pip. Therefore, you will need to first install Python and pip ([there are plenty of tutorials if needed](https://letmegooglethat.com/?q=how+to+install+python+and+pip)). Once installed, you can install cookiecutter with:

```bash
pip install cookiecutter
```

Now, you can simply download the project you want, fill the requested options, and the project will be created automatically.

### python-package

```bash
cookiecutter https://github.com/ClearPeaksSL/clearpeaks-programming-guidelines --directory="python-package"
```

## 👍 Coding guidelines

Check [CODING_GUIDELINES.md](CODING_GUIDELINES.md).

## ⚙️ Maintainers

Find any bug? We call it a feature 😎. Contact any of the maintainers:

| Name | Email |
| ---- | ----- |
| Victor Colome | victor.colome@clearpeaks.com |

Want to contribute? Check [CONTRIBUTING.md](CONTRIBUTING.md).
