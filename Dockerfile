FROM python:3.6-slim

WORKDIR /src/app

COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "./run.py"]