import os

from django_seven.deprecated_rules.new_helpers import validate_file, get_deprecated_rules


class RuleCheckMixin(object):

    maxDiff = None

    def assert_report(self, test_file, expected_report):
        current_folder, _ = os.path.split(os.path.abspath(test_file))
        filename = os.path.join(current_folder, 'checked_file.py')
        abs_path = os.path.abspath('.')

        report = validate_file(filename, get_deprecated_rules(), project_root=abs_path)

        self.assertDictEqual(report, expected_report)
