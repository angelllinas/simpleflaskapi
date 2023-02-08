FROM python:3.7.16

EXPOSE 5000

ADD . /app

WORKDIR /app

RUN pip3 --no-cache-dir install -r requirements.txt && \
    chgrp -R 0 /app && \
    chmod -R g=u /app

CMD ["python3", "src/app.py"]