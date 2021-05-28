# Python and Linux Version 
#FROM python:3.10.0a1-alpine3.12
#FROM python:3.8-slim
# issues with versions >3.6 with psycopg2
FROM python:3.6

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \  
exit    && pip install --no-cache-dir -r /app/requirements.txt 

# Working directory
WORKDIR /app

ADD . .

# for docker deployment 
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "coinedsolutions.wsgi:application"]

# for heroku deployment
CMD gunicorn coinedsolutions.wsgi:application --bind 0.0.0.0:$PORT