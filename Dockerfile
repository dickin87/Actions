FROM python:3.10

WORKDIR /home/dickin87/Actions

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "./example.py"]
