
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_REQUEST_RAW_POST_DATA
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedRequestRawPOSTDataRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_REQUEST_RAW_POST_DATA])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_REQUEST_RAW_POST_DATA['name']: {
                    'lines': [
                        {
                            'content': '    request_payload = request.raw_post_data\n',
                            'number': 6,
                            'filename': '/tests/deprecation_rules/deprecated_request_raw_post_data/checked_file.py'
                        }
                    ]
                }
            }
        )
