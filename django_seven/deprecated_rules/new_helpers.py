from collections import defaultdict

from django.conf import settings

from django_seven import CURRENT_DJANGO_VERSION, FUTURE_DJANGO_VERSION
from django_seven.compat.decorators import to_tuple
from django_seven.deprecated_rules.helpers import compile_regex
from django_seven.deprecated_rules.rules import DEPRECATED_RULES


def validating_regex(pattern, line):
    return pattern.search(line) is not None


def parse_file(filename, regex_rules):

    with open(filename) as f:
        for i, line in enumerate(f):
            for rule in regex_rules:
                if validating_regex(rule['compiled_regex'], line):
                    yield (rule, line, i+1)


def validate_file(filename, regex_rules, parse_progress=None, project_root=None):

    report = defaultdict(lambda: defaultdict(list))
    for rule, line, number in parse_file(filename, regex_rules):
        if parse_progress:
            parse_progress(filename, rule, line, number)
        if project_root:
            filename = filename.replace(project_root, '')
        report[rule['name']]['lines'].append({'content': line, 'number': number, 'filename': filename})
    return report


def is_relevant(rule):
    return to_tuple(CURRENT_DJANGO_VERSION) < to_tuple(rule['should_be_fixed_in']) <= to_tuple(FUTURE_DJANGO_VERSION)


def get_deprecated_rules():
    deprecated_rules = getattr(settings, 'DEPRECATED_RULES', DEPRECATED_RULES)
    relevant_rules = [rule for rule in deprecated_rules if is_relevant(rule)]
    compiled_rules = compile_regex(relevant_rules)

    return sorted(compiled_rules, key=lambda x: x['number'])
