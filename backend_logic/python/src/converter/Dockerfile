# base image for running python applications
FROM python:3.10-slim-bullseye

# to install os packages & preventing unnecessary packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential pkg-config ffmpeg \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

CMD ["python3", "consumer.py"]