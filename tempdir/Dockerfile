FROM python:3.8
RUN pip install flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/app.py
