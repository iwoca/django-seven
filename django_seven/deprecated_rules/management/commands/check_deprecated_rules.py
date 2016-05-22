from __future__ import absolute_import
import os

from django.core.management.base import BaseCommand

from django_seven.deprecated_rules import rules
from django_seven.deprecated_rules.helpers import aggregated_regex, is_excluded_dir, validate_file, is_excluded_file, \
    compile_regex


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ The idea is to freeze the migrations I have already processed in the new-style migration.
            If people are pushing new migrations, I will know, after saving what I already have managed,
            which ones I need to update.

            If the command is launched without arguments, I get the diff between actual migrations and the frozen ones
            With --save parameters, we save current migrations in the filesystem in a json file.
        """
        print('Checking deprecated rules...\n')
        errors = 0
        regex_rules = compile_regex(rules.REGEX_RULES)
        aggregated_regex_compiled = aggregated_regex(regex_rules)

        for rule in sorted(rules.REGEX_RULES.iteritems(), key=lambda x: x[1]['number']):
            print('{number}: {message}'.format(number=rule[1]['number'], message=rule[1]['message']))

        for dirName, subdirList, fileList in os.walk('.'):
            if not is_excluded_dir(dirName):
                for fname in [f for f in fileList if not is_excluded_file(f, dirName)]:
                    errors |= int(validate_file(fname, dirName, aggregated_regex_compiled, regex_rules))

        if errors:
            print('\nHave a look at http://django-seven.readthedocs.org/en/develop/deprecated-rules for more informations about these errors.\n')
        else:
            print('\nDeprecated rules respected. Good job \o/\n')
