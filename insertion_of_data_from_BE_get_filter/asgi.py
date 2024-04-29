"""
ASGI config for insertion_of_data_from_BE_get_filter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insertion_of_data_from_BE_get_filter.settings')

application = get_asgi_application()
