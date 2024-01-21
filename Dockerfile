FROM python:3.9-slim
LABEL authors="ofirzvishaboo"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "rest_app.py"]