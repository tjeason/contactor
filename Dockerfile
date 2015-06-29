FROM python:2.7

EXPOSE 9000

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV MAILGUN_API_KEY=abc1234
ENV MAILGUN_DOMAIN_NAME="sandboxtest.com"
ENV MANDRILL_API_KEY=abc1234

RUN python tests.py
