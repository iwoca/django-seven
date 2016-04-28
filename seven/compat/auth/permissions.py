import django


if django.VERSION < (1, 8):
    def get_permission_codename(action, opts):
        return '%s_%s' % (action, opts.object_name.lower())
else:
    from django.contrib.auth import get_permission_codename
