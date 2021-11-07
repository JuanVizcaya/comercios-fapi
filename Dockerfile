FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

COPY . /app/

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
