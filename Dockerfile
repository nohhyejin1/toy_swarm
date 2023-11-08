FROM python:3.8

COPY . /app
WORKDIR /app
RUN python3 -m venv venv && . venv/bin/activate
RUN pip3 install -r requirements.txt
WORKDIR /app/toy_swarm

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
EXPOSE 8000