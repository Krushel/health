FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY redis.conf /usr/local/etc/redis/redis.conf
