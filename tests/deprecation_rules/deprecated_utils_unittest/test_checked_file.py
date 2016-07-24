
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_UTILS_UNITTEST
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedDjangoSimpleJSonRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_UTILS_UNITTEST])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_UTILS_UNITTEST['name']: {
                    'lines': [
                        {
                            'content': 'from django.utils import unittest\n',
                            'number': 2,
                            'filename': '/tests/deprecation_rules/deprecated_utils_unittest/checked_file.py'
                        },
                        {
                            'content': 'import django.utils.unittest\n',
                            'number': 3,
                            'filename': '/tests/deprecation_rules/deprecated_utils_unittest/checked_file.py'
                        }
                    ]
                }
            }
        )
