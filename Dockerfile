FROM python:3.9

ADD ./BE /
ADD ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python" , "__init__.py"]

RUN pip install gunicorn[gevent]

EXPOSE 5001

#CMD gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:5001 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info