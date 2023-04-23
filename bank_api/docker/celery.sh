#!/bin/bash


cd backend
if [[ "${1}" == "celery" ]]; then
  celery --app tasks.tasks_celery:app worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app tasks.tasks_celery:app flower
#  celery flower --broker=redis://redis:6379/0
 fi


