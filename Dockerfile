FROM python:3.10.0-alpine
WORKDIR /app
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY /BackEnd/app
CMD ["uvicorn", "app.BackEnd:app", "--host", "0.0.0.0", "--port", "8000"]
