FROM python:3.7-alpine
LABEL author="mikebrumfield30@gmail.com"
RUN pip install --upgrade pip
WORKDIR /dynamoExport
COPY requirements.txt .
COPY dynamo.py .
COPY export_to_s3.py .
COPY util.py .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3",  "export_to_s3.py"]