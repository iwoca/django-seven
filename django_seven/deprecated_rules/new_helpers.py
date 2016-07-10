import re
from collections import defaultdict


def validating_regex(regex, line):
    pattern = re.compile(regex)
    return pattern.search(line) is not None


def parse_file(filename, regex_rules):

    with open(filename) as f:
        for i, line in enumerate(f):
            for rule in regex_rules:
                if validating_regex(rule['regex'], line):
                    yield (rule['name'], line, i+1)


def validate_file(filename, regex_rules, parse_progress=None):

    report = defaultdict(lambda: defaultdict(list))
    for rule_name, line, number in parse_file(filename, regex_rules):
        if parse_progress:
            parse_progress(filename, rule_name, file)
        report[rule_name]['lines'].append({'content': line, 'number': number})
    return report
