FROM python:3.8
LABEL Description="baby_try" VERSION='1.0'

COPY server.py .
COPY secret.py .

RUN chmod +x server.py

EXPOSE 12345

CMD ["python", "server.py"]
