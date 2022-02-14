FROM python:3-alpine
ADD ./app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]
