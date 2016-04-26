import django

if django.VERSION < (1, 6):
    PASSWORD_URL_RESET_COMPAT = r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$'
else:
    PASSWORD_URL_RESET_COMPAT = r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$'
