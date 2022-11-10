FROM python:3.9

COPY . /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy
RUN sh pre_start.sh

EXPOSE 8050
CMD ["python", "app.py"]