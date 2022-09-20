FROM  python:3.10

WORKDIR /mysite
COPY . .
RUN pip install -r requirements.txt
CMD ["sh","-c","python manage.py runserver 0.0.0.0:8000"]
