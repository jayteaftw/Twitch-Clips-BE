FROM python:3.9

ADD ./BE /
ADD ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python" , "debug_run.py"]