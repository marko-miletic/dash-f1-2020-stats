FROM python:3.9

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . .
RUN  pip install pipenv  \
&& pipenv requirements > requirements.txt \
&& pip install -r requirements.txt

EXPOSE 8050

CMD bash pre_start.sh && python app.py