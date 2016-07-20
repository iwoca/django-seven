
from collections import defaultdict


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
