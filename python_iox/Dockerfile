FROM python:3.6-alpine

RUN apk --no-cache add build-base libffi-dev openssl-dev openssl

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY python_web_server.py ./

COPY start.sh /opt/apps/
