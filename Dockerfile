FROM python:3.9.0-alpine

ADD ankify.py requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["./ankify.py", "-"]

