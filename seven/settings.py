
from django.conf import settings


if not hasattr(settings, 'CURRENT_DJANGO_VERSION'):
    CURRENT_DJANGO_VERSION = (1, 4)

if not hasattr(settings, 'FUTURE_DJANGO_VERSION'):
    CURRENT_DJANGO_VERSION = (1, 9)
