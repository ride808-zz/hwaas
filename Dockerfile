FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080 8787
CMD ["gunicorn", "-w 4", "main:app"]
