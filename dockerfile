FROM python:3.9.19

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt