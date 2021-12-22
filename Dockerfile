FROM python:3

WORKDIR /usr/src/app

COPY req.txt .
COPY entrypoint.sh .

RUN pip install -r req.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

