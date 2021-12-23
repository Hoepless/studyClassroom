FROM python:3

WORKDIR /app

COPY req.txt .
COPY entrypoint.sh .

RUN pip install -r req.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]

