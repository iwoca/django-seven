
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import DEPRECATED_TRANSACTION_SYSTEM
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestDeprecatedTransactionSystemRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[DEPRECATED_TRANSACTION_SYSTEM])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                DEPRECATED_TRANSACTION_SYSTEM['name']: {
                    'lines': [
                        {
                            'content': '@transaction.commit_on_success()\n',
                            'number': 7,
                            'filename': '/tests/deprecation_rules/deprecated_transaction_system/checked_file.py'
                        },
                        {
                            'content': '    with commit_on_success():\n',
                            'number': 13,
                            'filename': '/tests/deprecation_rules/deprecated_transaction_system/checked_file.py'
                        },
                        {
                            'content': '    @commit_on_success()\n',
                            'number': 18,
                            'filename': '/tests/deprecation_rules/deprecated_transaction_system/checked_file.py'
                        },
                        {
                            'content': '@transaction.commit_manually()\n',
                            'number': 23,
                            'filename': '/tests/deprecation_rules/deprecated_transaction_system/checked_file.py'
                        }
                    ]
                }
            }
        )
