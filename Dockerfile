FROM python:3.6

ENV FLASK_APP "simpleapp.py"
ENV FLASK_ENV "development"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 5000

CMD flask run --host=0.0.0.0
