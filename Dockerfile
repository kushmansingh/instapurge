FROM python:2.7

COPY main.py /usr/src/instapurge/
COPY requirements.txt /usr/src/instapurge/
COPY instapurge/ /usr/src/instapurge/instapurge
WORKDIR /usr/src/instapurge

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]