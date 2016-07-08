import re
from collections import defaultdict


def validating_regex(regex, line):
    pattern = re.compile(regex)
    return pattern.search(line) is not None


def validate_file(filename, regex_rules):

    report = defaultdict(lambda: defaultdict(list))

    with open(filename) as f:
        for i, line in enumerate(f):
            for rule in regex_rules:
                if validating_regex(rule['regex'], line):
                    report[rule['name']]['lines'].append(i+1)
    return report
