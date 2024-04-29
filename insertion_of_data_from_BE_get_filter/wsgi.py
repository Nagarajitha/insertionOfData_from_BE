"""
WSGI config for insertion_of_data_from_BE_get_filter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insertion_of_data_from_BE_get_filter.settings')

application = get_wsgi_application()
