FROM python:3.13
WORKDIR /usr/src/JWT_test_task
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt -y update && \
    apt install -y python3-dev libpq-dev python3-dev
RUN pip install -U pip uwsgi
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .. .
ENTRYPOINT ["/usr/src/JWT_test_task/entrypoint.sh"]


