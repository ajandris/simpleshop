"""
Gunicorn configuration file for simpleshop.
https://docs.gunicorn.org/en/stable/configure.html
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Ensure .env is loaded
load_dotenv(BASE_DIR / ".env")

# WSGI Application entry point
wsgi_app = "simpleshop.wsgi:application"

# Network binding
host = os.environ.get("HOST")
port = os.environ.get("PORT")
bind = f"{host}:{port}"

# Worker processes
workers = int(os.environ.get("WEB_CONCURRENCY"))
threads = int(os.environ.get("GUNICORN_THREADS"))
worker_class = os.environ.get("GUNICORN_WORKER_CLASS")

# Worker recycling to mitigate memory leaks
max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS"))
max_requests_jitter = int(os.environ.get("GUNICORN_MAX_REQUESTS_JITTER"))

# Timeouts
timeout = int(os.environ.get("GUNICORN_TIMEOUT"))
keepalive = int(os.environ.get("GUNICORN_KEEPALIVE"))

# Logging
accesslog = os.environ.get("GUNICORN_ACCESSLOG")
errorlog = os.environ.get("GUNICORN_ERRORLOG")
loglevel = os.environ.get("GUNICORN_LOGLEVEL")
capture_output = True
