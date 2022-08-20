FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
# COPY requirements.txt /code/
RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "-r", "/code/requirements.txt"]