FROM python:3.7

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /app

COPY ./deneb.py /app

CMD ["python", "/app/deneb.py"]
