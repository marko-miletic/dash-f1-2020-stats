#! /usr/bin/env bash

#Start docker container
docker compose up --force-recreate -d
sleep 5

# Run migrations
alembic upgrade head

python3 pre_start.py

# Run API
python3 app.py
