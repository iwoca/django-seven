from functools import wraps

from seven import settings as seven_settings


def to_tuple(version):
    return tuple(map(lambda x: int(x), version.split('.')))


def available_on(min_supported_version, max_supported_version):
    def wrapped_parameters(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if (to_tuple(seven_settings.CURRENT_DJANGO_VERSION) > to_tuple(min_supported_version)) and\
                    (to_tuple(seven_settings.FUTURE_DJANGO_VERSION) < to_tuple(max_supported_version)):
                return func(*args, **kwargs)
            return Exception('You cannot use {function_name} in your context'.format(function_name=str(func)))
        return inner
    return wrapped_parameters
