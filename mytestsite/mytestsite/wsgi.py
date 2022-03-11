"""
WSGI config for mytestsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

ADMIN_ENV_NAME = "ADMIN_ENV"
LOCAL = "LOCAL"
STAGING = "STAGING"
DOCKER_LOCAL = "DOCKER_LOCAL"
DOCKER_STAGING = "DOCKER-LOCAL"
DOCKER_STAGING = "DOCKER-STAGING"


admin_env = os.getenv(ADMIN_ENV_NAME, LOCAL)
if admin_env == LOCAL:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings.local')
elif admin_env == STAGING:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings.staging')
elif admin_env == DOCKER_LOCAL:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings.docker-local')
elif admin_env == DOCKER_STAGING:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings.docker-staging')

application = get_wsgi_application()
