import os

from django.test import TestCase
from django_seven.deprecated_rules.new_helpers import validate_file


RULES = [
    {
        'name': 'boolean_default',
        'message': 'BooleanField message',
        'regex': r'models\.BooleanField(?!(\(.*(default=)+.*\)))',
        'number': '1601',
    }
]


class TestBooleanFieldDefaultRule(TestCase):

    def test_validate_rule(self):
        current_folder, _ = os.path.split(os.path.abspath(__file__))
        filename = os.path.join(current_folder, 'checked_file.py')
        report = validate_file(filename, RULES)

        self.assertDictEqual(
            {'deprecated':
                 report
             },
            {
                'deprecated': {
                    'boolean_default': {
                        'lines': [
                            {
                                'content': '    bad_boolean_field = models.BooleanField()\n',
                                'number': 5
                            }
                        ]
                    }
                }
            })
