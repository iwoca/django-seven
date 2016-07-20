#!/usr/bin/python
import os
import re
from . import rules


EXCLUDED_DIRS = []
EXCLUDED_SUB_PATHS = []
EXCLUDED_SPECIFIC_FILE = []
EXCLUDED_FILE_EXTENSIONS = []


def validating_regex(pattern, st):
    return pattern.match(st) is not None


def is_excluded_dir(dir_name):
    return any([excluded_subpath in dir_name for excluded_subpath in EXCLUDED_SUB_PATHS])\
        or any([dir_name.startswith('./' + excluded_dir) for excluded_dir in EXCLUDED_DIRS])


def is_excluded_file(file_name, dir_name):
    full_file_name = os.path.join(dir_name, file_name)
    return any([file_name.endswith(excluded_file) for excluded_file in EXCLUDED_FILE_EXTENSIONS])\
        or any([excluded_file in full_file_name for excluded_file in EXCLUDED_SPECIFIC_FILE])


def compile_regex(regex_rules):
    for rule in regex_rules:
        rule['compiled_regex'] = re.compile(rule['regex'])

    return regex_rules


def validate_file(file_name, dir_name, aggregated_regex_compiled, regex_rules):
    errors = False
    full_file_name = os.path.join(dir_name, file_name)

    with open(full_file_name) as fil:
        for i, line in enumerate(fil):
            if validating_regex(aggregated_regex_compiled, line):
                for rule in regex_rules.values():
                    if validating_regex(rule['compiled_regex'], line):
                        print(full_file_name)
                        print("{number}: {message}".format(number=rule['number'], message=rule['message']))
                        print("L{line_number}: {line}".format(line_number=i+1, line=line))
                        errors = True

    return errors
