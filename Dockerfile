FROM python:3.10.0

WORKDIR /Django-Blog-Template-main

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000