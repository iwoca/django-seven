#!/usr/bin/python
import os
import re


EXCLUDED_DIRS = []
EXCLUDED_SUB_PATHS = []
EXCLUDED_SPECIFIC_FILE = []
EXCLUDED_FILE_EXTENSIONS = []


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
