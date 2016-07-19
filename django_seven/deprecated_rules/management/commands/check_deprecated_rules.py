from __future__ import absolute_import
import os

from django.core.management.base import BaseCommand

from django_seven.deprecated_rules import rules
from django_seven.deprecated_rules.helpers import is_excluded_dir, is_excluded_file, compile_regex
from django_seven.deprecated_rules.new_helpers import validate_file


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ The idea is to freeze the migrations I have already processed in the new-style migration.
            If people are pushing new migrations, I will know, after saving what I already have managed,
            which ones I need to update.

            If the command is launched without arguments, I get the diff between actual migrations and the frozen ones
            With --save parameters, we save current migrations in the filesystem in a json file.
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
