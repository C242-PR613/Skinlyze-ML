FROM python:3.12

WORKDIR /skinlyze-ml-deployment/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python", "app.py"]