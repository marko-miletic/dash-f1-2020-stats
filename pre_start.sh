#! /usr/bin/env bash

#Start docker container
docker compose --force-recreate -d --wait
sleep 1

# Run migrations
alembic upgrade head

python3 pre_start.py

# Run API
#python3 app.py
