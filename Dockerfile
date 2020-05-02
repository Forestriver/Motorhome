# base image
FROM python: 3.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0

# psycopg2 installation
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps


# dependencies
COPY ./requirements.txt .
RUN pip install  -r requirements.txt

#project copy
COPY . .

RUN adduser -D myuser
USER myuser
# Run application
CMD gunicorn motorhome.wsgi:application --bind 0.0.0.0:$PORT
