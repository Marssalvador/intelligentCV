#!/usr/bin/env bash
source venv/Scripts/activate   # o venv/bin/activate en Unix
cd backend
python manage.py runserver 0.0.0.0:8000
