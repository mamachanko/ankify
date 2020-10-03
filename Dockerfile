FROM python:3.8.6

WORKDIR /src

COPY requirements*.txt /src

RUN pip install \
    --no-cache-dir \
    -r /src/requirements.txt \
    -r /src/requirements-dev.txt
