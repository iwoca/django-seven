
NEW_URL_TEMPLATETAG_SYNTAX = {
    'name': 'new_url_templatetag_syntax',
    'message': 'Urls should be called with view name between quotes. Previous syntax was authorizing without quotes',
    'regex': r'(%\s+url+\s)([0-9a-z_:]+)',
    'number': '1501',
    'should_be_fixed_in': '1.5',
}

DEPRECATED_GENERIC_FBV = {
    'name': 'deprecated_generic_fbv',
    'message': 'Deprecated fbv direct_to_template/redirect_to, should be replaced by TemplateView/RedirectView',
    'regex': r'(direct_to_template)|(redirect_to\()',
    'number': '1502',
    'should_be_fixed_in': '1.5',
}

DEPRECATED_DJANGO_SIMPLEJSON = {
    'name': 'deprecated_django_simplejson',
    'message': 'Deprecated django.utils.simplejson. Use standard json library (has speedups from python 2.7',
    'regex': r'django\.utils.*simplejson',
    'number': '1503',
    'should_be_fixed_in': '1.5',
}

DEPRECATED_ADMIN_MEDIA_MODULE = {
    'name': 'deprecated_admin_media_module',
    'message': 'Deprecated adminmedia module. Use staticfiles.',
    'regex': r'\s+(adminmedia)|(admin_media_prefix)\s+',
    'number': '1504',
    'should_be_fixed_in': '1.5',
}

BOOLEAN_DEFAULT = {
    'name': 'boolean_default',
    'message': ('models.BooleanField has to be initialised with default parameter, as implicit default has changed '
                'between Django 1.4 (False) and 1.6 (None).'),
    'regex': r'models\.BooleanField(?!(\(.*(default=)+.*\)))',
    'number': '1601',
    'should_be_fixed_in': '1.6',
}

DEPRECATED_DJANGO_LOCAL_FLAVOR_MODULE = {
    'name': 'deprecated_django_local_flavor_module',
    'message': 'Deprecated django.contrib.localflavor module (now third-party lib). Use localflavor instead.',
    'regex': r'django\.contrib.*localflavor',
    'number': '1602',
    'should_be_fixed_in': '1.6',
}

DEPRECATED_TRANSACTION_SYSTEM = {
    'name': 'deprecated_transaction_system',
    'message': 'Transaction management has been completely changed. atomic is replacing old commit_on_success and other utils.',
    'regex': r'((@|with\s)transaction\.(commit_on_success|commit_manually))',
    'number': '1603',
    'should_be_fixed_in': '1.6',
}

DEPRECATED_REQUEST_RAW_POST_DATA = {
    'name': 'deprecated_request_raw_post_data',
    'message': 'Deprecated request.raw_post_data, replaced by request.body',
    'regex': r'request\.raw_post_data',
    'number': '1604',
    'should_be_fixed_in': '1.6',
}

DEPRECATED_UTILS_UNITTEST = {
    'name': 'deprecated_utils_unittest',
    'message': 'Deprecated django.utils.unittest module. Use unittest module instead.',
    'regex': r'django\.utils\.unittest',
    'number': '1701',
    'should_be_fixed_in': '1.7',
}

DEPRECATED_MIMETYPE_HTTPRESPONSE_PARAMETER = {
    'name': 'deprecated_mimetype_httpresponse_parameter',
    'message': 'Deprecated mimetype parameter for HTTPResponse. Use content_type instead.',
    'regex': r'mimetype\=',
    'number': '1702',
    'should_be_fixed_in': '1.7',
}

DEPRECATED_GET_QUERY_SET_FUNCTION = {
    'name': 'deprecated_get_query_set_function',
    'message': "Managers shouldn't define get_query_set function anymore but get_queryset.",
    'regex': r'def get_query_set\(',
    'number': '1801',
    'should_be_fixed_in': '1.8',
}

DEPRECATED_RULES = [

    # Django 1.5
    NEW_URL_TEMPLATETAG_SYNTAX,
    DEPRECATED_GENERIC_FBV,
    DEPRECATED_DJANGO_SIMPLEJSON,
    DEPRECATED_ADMIN_MEDIA_MODULE,

    # Django 1.6
    BOOLEAN_DEFAULT,
    DEPRECATED_DJANGO_LOCAL_FLAVOR_MODULE,
    DEPRECATED_TRANSACTION_SYSTEM,
    DEPRECATED_REQUEST_RAW_POST_DATA,

    # Django 1.7
    DEPRECATED_UTILS_UNITTEST,
    DEPRECATED_MIMETYPE_HTTPRESPONSE_PARAMETER,

    # Django 1.8
    DEPRECATED_GET_QUERY_SET_FUNCTION
]
