#!/bin/bash

# Load environment variables from .env file
source /.env
# Set python path
set -e
export PYTHONPATH=/auth/:$PYTHONPATH

# Wait for 10 seconds before starting the app for database connection
#sleep 5

# Start the FastAPI application
alembic revision --autogenerate -m "..."
alembic upgrade head

uvicorn app.main:app --host ${FASTAPI_HOST} --reload --port ${FASTAPI_PORT}
