# gunicorn_config.py

import multiprocessing

# Gunicorn settings
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

# Logging
accesslog = "-" 
errorlog = "./error.log"   
loglevel = "info"


proc_name = "leaf-shop-django" 

# Security
secure_scheme_headers = {
    "X-Forwarded-Proto": "https" 
}

# Worker timeout
timeout = 120 

# Django-specific settings
preload_app = True 
