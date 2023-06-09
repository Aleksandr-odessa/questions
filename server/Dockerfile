From python:3.10.6

WORKDIR /server/

COPY . /server/
RUN apt-get update && \
    apt-get install -y libpq-dev gcc
RUN pip install -r requirements.txt

EXPOSE 8000