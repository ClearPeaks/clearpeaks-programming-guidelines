# Set base image
FROM python:3.7

# Set docker folder
WORKDIR /{{ cookiecutter.project_slug }}

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy content to docker image
COPY {{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }} 

# Command to run on container start
CMD [ "python", "{{ cookiecutter.project_slug }}" ]
