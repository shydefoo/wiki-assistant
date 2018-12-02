FROM python:3

WORKDIR /app

COPY data /app
COPY src /app
COPY wait-for-it.sh /app
COPY requirements.txt /app


RUN pip install -r requirements.txt
RUN chmod 777 wait-for-it.sh
EXPOSE 5000

ENV HOST db_service
ENV PORT_NUM 3306
ENV USERNAME root
ENV TARGET_DB wiki_database
ENV PYTHONPATH "${PYTHONPATH}:./src"

CMD ["./wait-for-it.sh", "db_service:3306", "--", "gunicorn", "--bind", "0.0.0.0", "-w", "4", "webapp:app"]