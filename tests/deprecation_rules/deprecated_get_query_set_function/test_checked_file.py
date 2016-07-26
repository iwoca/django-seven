
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_GET_QUERY_SET_FUNCTION
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedGetQuerySetFunctionRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_GET_QUERY_SET_FUNCTION])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_GET_QUERY_SET_FUNCTION['name']: {
                    'lines': [
                        {
                            'content': "    def get_query_set(self):\n",
                            'number': 8,
                            'filename': '/tests/deprecation_rules/deprecated_get_query_set_function/checked_file.py'
                        },
                        {
                            'content': "        return super(MyModelManager, self).get_query_set()\n",
                            'number': 9,
                            'filename': '/tests/deprecation_rules/deprecated_get_query_set_function/checked_file.py'
                        }
                    ]
                }
            }
        )
