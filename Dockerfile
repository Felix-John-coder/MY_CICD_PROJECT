FROM python:3.11-slim

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python" ]
CMD [ "src/app.py" ]