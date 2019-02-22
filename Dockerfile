FROM python:3.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD . /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements/local.txt
EXPOSE 8000
