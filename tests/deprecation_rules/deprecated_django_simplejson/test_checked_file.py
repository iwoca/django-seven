
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_DJANGO_SIMPLEJSON
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedDjangoSimpleJSonRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_DJANGO_SIMPLEJSON])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                'deprecated_django_simplejson': {
                    'lines': [
                        {
                            'content': 'from django.utils import simplejson\n',
                            'number': 2,
                            'filename': '/tests/deprecation_rules/deprecated_django_simplejson/checked_file.py'
                        },
                        {
                            'content': 'import django.utils.simplejson\n',
                            'number': 3,
                            'filename': '/tests/deprecation_rules/deprecated_django_simplejson/checked_file.py'
                        }
                    ]
                }
            }
        )
