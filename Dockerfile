FROM python:3

WORKDIR /app
COPY src /app/src
COPY data /app/data
COPY wait-for-it.sh /app
COPY requirements.txt /app


RUN pip install -r requirements.txt
RUN chmod 777 wait-for-it.sh

ENV HOST db_service
ENV PORT_NUM 3306
ENV USERNAME root
ENV TARGET_DB wiki_database
ENV PYTHONPATH "${PYTHONPATH}:src"

CMD ["./wait-for-it.sh", "db_service:3306", "--", "gunicorn", "--bind", "0.0.0.0", "--threads", "4", "--timeout", "1000", "webapp:app" ]