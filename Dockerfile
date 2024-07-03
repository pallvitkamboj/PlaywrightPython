# FROM python:latest
FROM --platform=linux/amd64 python:latest



WORKDIR /app

COPY requirements.txt ./
COPY package.json ./
COPY pytest ./pytest



RUN pip install pytest-playwright
RUN playwright install  
RUN pip3 install --no-cache-dir -r requirements.txt
RUN playwright install-deps 



WORKDIR /app/pytest


CMD [ "pytest" ]




