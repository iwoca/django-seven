
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_ADMIN_MEDIA_MODULE
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedAdminMediaModuleRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_ADMIN_MEDIA_MODULE])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_ADMIN_MEDIA_MODULE['name']: {
                    'lines': [
                        {
                            'content': '{% adminmedia %}\n',
                            'number': 2,
                            'filename': '/tests/deprecation_rules/deprecated_admin_media_module/checked_file.py'
                        },
                        {
                            'content': '{% admin_media_prefix %}\n',
                            'number': 3,
                            'filename': '/tests/deprecation_rules/deprecated_admin_media_module/checked_file.py'
                        }
                    ]
                }
            }
        )
