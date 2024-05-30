FROM python:3.10-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


# docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app
