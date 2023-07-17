FROM python:3.11.1
WORKDIR /csit-mini-challenge-3
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python main.py