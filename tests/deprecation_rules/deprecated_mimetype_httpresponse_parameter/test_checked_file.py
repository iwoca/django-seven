
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_MIMETYPE_HTTPRESPONSE_PARAMETER
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedTransactionSystemRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_MIMETYPE_HTTPRESPONSE_PARAMETER])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_MIMETYPE_HTTPRESPONSE_PARAMETER['name']: {
                    'lines': [
                        {
                            'content': "    return HttpResponse(mimetype='application/json')\n",
                            'number': 8,
                            'filename': '/tests/deprecation_rules/deprecated_mimetype_httpresponse_parameter/checked_file.py'
                        }
                    ]
                }
            }
        )
