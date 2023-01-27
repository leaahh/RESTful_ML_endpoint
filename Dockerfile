# Dockerfile to build a flask app
FROM python:3.9

WORKDIR /usr/src/app

ENV FLASK_APP="app"

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .

EXPOSE 5000 

CMD ["python", "-m", "flask", "run"]
