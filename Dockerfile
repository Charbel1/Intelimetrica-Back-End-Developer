FROM python:3

WORKDIR /usr/src/app
COPY req.txt ./
RUN pip install -r req.txt
COPY . .

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]