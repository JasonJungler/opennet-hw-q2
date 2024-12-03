FROM python:3.13-rc-slim

WORKDIR /app

COPY ./src /app/src
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py", "receive"]
