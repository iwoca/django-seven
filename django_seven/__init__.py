
from django.conf import settings


CURRENT_DJANGO_VERSION = getattr(settings, 'CURRENT_DJANGO_VERSION', '1.4')
FUTURE_DJANGO_VERSION = getattr(settings, 'FUTURE_DJANGO_VERSION', '1.9')
