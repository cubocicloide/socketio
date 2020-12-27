FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache libffi-dev postgresql-client postgresql-contrib postgresql-dev bash g++ linux-headers coreutils

RUN apk add --no-cache make

ADD ./requirements.txt /tmp/

# Install PyPi dependencies
WORKDIR /tmp
RUN pip install --upgrade pip && pip install cython
RUN pip install uvicorn[standard]
RUN pip install -r requirements.txt 

RUN apk del build-deps

ADD . /code/

RUN mkdir -p /storage/static
RUN mkdir -p /storage/media

RUN chmod -R a+rw /storage

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /code/

COPY wait-for-postgres.sh /usr/local/bin/wait-for-postgres.sh
RUN chmod +x /usr/local/bin/wait-for-postgres.sh

EXPOSE 8000
EXPOSE 8001

CMD /./entrypoint.sh
