import os

from django.test import TestCase
from django_seven.deprecated_rules.helpers import compile_regex
from django_seven.deprecated_rules.new_helpers import validate_file


RULES = [
    {
        'name': 'boolean_default',
        'message': 'BooleanField message',
        'regex': r'models\.BooleanField(?!(\(.*(default=)+.*\)))',
        'number': '1601',
    }
]


class RuleCheckMixin(object):

    def assert_report(self, expected_report):
        current_folder, _ = os.path.split(os.path.abspath(__file__))
        filename = os.path.join(current_folder, 'checked_file.py')
        abs_path = os.path.abspath('.')

        regex_rules = compile_regex(RULES)
        report = validate_file(filename, regex_rules, project_root=abs_path)

        self.assertDictEqual(report, expected_report)


class TestBooleanFieldDefaultRule(RuleCheckMixin, TestCase):

    def test_validate_rule(self):
        self.assert_report(
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

