from __future__ import absolute_import
import os

from django.core.management.base import BaseCommand

from django_seven.deprecated_rules import rules
from django_seven.deprecated_rules.helpers import is_excluded_dir, is_excluded_file, compile_regex
from django_seven.deprecated_rules.new_helpers import validate_file


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        This management command applies all deprecated rules defined in rules module.
        Every non-respected rule will have a report displayed with some explanations to fix it:
        - The impacted file,
        - The rule number, with a human description
        - The line number, and the line copy.

        $ ./manage.py check_deprecated_rules

        ./core/models.py
        1601: models.BooleanField has to be initialised with default parameter,
              as implicit default has changed between Django 1.4 (False) and 1.6 (None).
        L6:     boolean_field = models.BooleanField()

        """
        print('Check deprecated rules...\n')
        regex_rules = compile_regex(rules.REGEX_RULES)

        for rule in sorted(rules.REGEX_RULES, key=lambda x: x['number']):
            print('{number}: {message}'.format(number=rule['number'], message=rule['message']))

        report = {}

        def progress_fn(filename, rule, line, number):
            print(filename)
            print("{number}: {message}".format(number=rule['number'], message=rule['message']))
            print("L{line_number}: {line}".format(line_number=number, line=line))

        for dirName, subdirList, fileList in os.walk('.'):
            if not is_excluded_dir(dirName):
                for fname in [f for f in fileList if not is_excluded_file(f, dirName)]:
                    file_report = validate_file(os.path.join(dirName, fname), regex_rules, progress_fn)
                    report.update(file_report)

        if len(report) > 0:
            print('\nHave a look at http://django-seven.readthedocs.org/en/develop/deprecated-rules for more informations about these errors.\n')
        else:
            print('\nDeprecated rules respected. Good job \o/\n')
