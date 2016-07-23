
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import BOOLEAN_DEFAULT
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestBooleanFieldDefaultRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[BOOLEAN_DEFAULT])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                'boolean_default': {
                    'lines': [
                        {
                            'content': '    bad_boolean_field = models.BooleanField()\n',
                            'number': 5,
                            'filename': '/tests/deprecation_rules/boolean_field_default_value/checked_file.py'
                        }
                    ]
                }
            }
        )

