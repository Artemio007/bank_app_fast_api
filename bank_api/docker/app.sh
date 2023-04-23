#!/bin/bash

cd backend
#alembic revision --autogenerate -m "docker_migrate"
alembic upgrade head

uvicorn main:app --host 0.0.0.0 --port 8000

# shellcheck disable=SC2103
#cd ..
