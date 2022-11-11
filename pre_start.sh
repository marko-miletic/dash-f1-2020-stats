#! /usr/bin/env bash

# Run Alembic scrip
sleep 5
alembic upgrade head

# Fill with test data
sleep 5
python3 pre_start.py
