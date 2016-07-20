import django


if django.VERSION < (1, 8):
    ALL_FIELDS = None
else:
    ALL_FIELDS = '__all__'
