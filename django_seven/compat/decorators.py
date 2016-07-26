from functools import wraps

from django.conf import settings


def to_tuple(version):
    return tuple(map(lambda x: int(x), version.split('.')))


def available_on(min_supported_version, max_supported_version):
    def wrapped_parameters(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if (to_tuple(settings.SEVEN_CURRENT_DJANGO_VERSION) > to_tuple(min_supported_version)) and\
                    (to_tuple(settings.SEVEN_FUTURE_DJANGO_VERSION) < to_tuple(max_supported_version)):
                return func(*args, **kwargs)
            raise Exception('You cannot use {function_name} in your context'.format(function_name=str(func)))
        return inner
    return wrapped_parameters
