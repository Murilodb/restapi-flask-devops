FROM python:3.12.16-alpine3.23
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY wsgi.py .
COPY config.py .
COPY applications applications
CMD ["python", "wsgi.py"]
EXPOSE 5000
