import collections
import os

from django.test import TestCase
import re

RULES = [{
        'name': 'boolean_default',
        'message': 'BooleanField message',
        'regex': r'models\.BooleanField(?!(\(.*(default=)+.*\)))',
        'number': '1601',
        'old_django_version': '1.5',
        'new_django_version': '1.6'
}]


def validating_regex(regex, line):
    pattern = re.compile(regex)
    return pattern.search(line) is not None


def validate_file(filename, regex_rules):

    report = collections.defaultdict(lambda: collections.defaultdict(list))

    with open(filename) as f:
        for i, line in enumerate(f):
            for rule in regex_rules:
                if validating_regex(rule['regex'], line):
                    report[rule['name']]['lines'].append(i+1)
    return report


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
                        'lines': [5]
                    }
                }
            })
