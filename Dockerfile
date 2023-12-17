FROM python:3.8.0-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x run.sh
ENTRYPOINT ["sh", "run.sh"]
EXPOSE 5000
