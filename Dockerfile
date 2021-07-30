FROM python:3.9.2-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /probelyLearn

COPY requirements.txt requirements.txt

RUN apk update && \
apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


#docker build --tag python-django .  --> create image
# docker run --publish 8000:8000 python-django  --> create container for the python-django image

