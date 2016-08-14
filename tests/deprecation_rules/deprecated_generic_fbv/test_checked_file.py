
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_GENERIC_FBV
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedGenericFBVRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_GENERIC_FBV])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_GENERIC_FBV['name']: {
                    'lines': [
                        {
                            'content': "    url(r'^direct_url$', direct_to_template('direct_template.html')),\n",
                            'number': 3,
                            'filename': '/tests/deprecation_rules/deprecated_generic_fbv/checked_file.py'
                        },
                        {
                            'content': "    url(r'^redirect_url$', redirect_to('redirect_template.html')),\n",
                            'number': 4,
                            'filename': '/tests/deprecation_rules/deprecated_generic_fbv/checked_file.py'
                        }
                    ]
                }
            }
        )
