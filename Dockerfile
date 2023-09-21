FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r req.txt

ENTRYPOINT ["python"]

EXPOSE 5003

CMD ["application.py"]