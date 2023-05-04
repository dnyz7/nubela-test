FROM python:3.7-alpine
WORKDIR /app
COPY . .
ENTRYPOINT ["python","-u", "app.py"]