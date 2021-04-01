# python 3.8
FROM python:3.8

# load pipenv
RUN pip install pipenv

# update apt-get
RUN apt-get update

# install rapper
RUN apt-get install -y raptor2-utils

# set up prroject directory
ENV PROJECT_DIR /usr/local/src/webapp

# set workdir as the project dir
WORKDIR ${PROJECT_DIR}

#copy all the files
COPY . .

# install packages
# --system -> dont create venv but install them in containers system python
# --deploy -> die if Pipfile.lock is out of date
RUN pipenv install --system --deploy

#Expose the required port
EXPOSE 5000

#Run the command
CMD python run.py