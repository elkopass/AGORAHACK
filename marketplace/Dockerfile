FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
# COPY requirements.txt /code/
RUN ["pip3", "install", "-r", "/code/requirements.txt"]
EXPOSE 8001
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]