from django import VERSION as DJANGO_VERSION


def get_errors(error_dict):
    if DJANGO_VERSION >= (1, 7):
        return error_dict.as_data()
    else:
        return error_dict.as_text()