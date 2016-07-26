
from django.test import TestCase
from django.test.utils import override_settings
from django_seven.deprecated_rules.rules import NEW_URL_TEMPLATETAG_SYNTAX
from tests.deprecation_rules.mixins import RuleCheckMixin


class TestNewURLTemplateTagSyntaxRule(RuleCheckMixin, TestCase):

    @override_settings(DEPRECATED_RULES=[NEW_URL_TEMPLATETAG_SYNTAX])
    def test_validate_rule(self):
        self.assert_report(__file__,
            {
                NEW_URL_TEMPLATETAG_SYNTAX['name']: {
                    'lines': [
                        {
                            'content': '<form action="{% url myview %}" method="POST">\n',
                            'number': 2,
                            'filename': '/tests/deprecation_rules/new_url_templatetag_syntax/checked_file.py'
                        }
                    ]
                }
            }
        )
