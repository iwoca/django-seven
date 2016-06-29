import os

from django.test import TestCase

RULE = {
    'boolean_default': {
        'message': 'BooleanField message',
        'regex': r'.*models\.BooleanField(?!(\(.*(default=)+.*\))).*',
        'number': '1601',
        'old_django_version': '1.5',
        'new_django_version': '1.6'
    }
}

def validate_file(filename, regex_rules):
    pass


class TestBooleanFieldDefaultRule(TestCase):

    def test_validate_rule(self):
        filename = os.path.join('.', 'checked_file.py')
        report = validate_file(filename, [RULE])

        self.assertDictEqual(
            report,
            {
                'deprecated': {
                    'boolean_default': {
                        'lines': [5]
                    }
                }
            })
