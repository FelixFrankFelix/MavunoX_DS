FROM python:3.12.0-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

EXPOSE 8000

CMD ["uvicorn","main:app", "-host", "0.0.0.0", "--port","8000"]