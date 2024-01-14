FROM python:3.11.7-slim
#docker pull python:3.9.18-slim-bullseye
WORKDIR /flask-docker

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]