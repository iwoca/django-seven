
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_DJANGO_LOCAL_FLAVOR_MODULE
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedDjangoLocalFlavorModuleRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_DJANGO_LOCAL_FLAVOR_MODULE])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_DJANGO_LOCAL_FLAVOR_MODULE['name']: {
                    'lines': [
                        {
                            'content': 'from django.contrib import localflavor\n',
                            'number': 2,
                            'filename': '/tests/deprecation_rules/deprecated_django_local_flavor_module/checked_file.py'
                        },
                        {
                            'content': 'import django.contrib.localflavor\n',
                            'number': 3,
                            'filename': '/tests/deprecation_rules/deprecated_django_local_flavor_module/checked_file.py'
                        }
                    ]
                }
            }
        )
