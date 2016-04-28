from django.test import TestCase
from django.test.utils import override_settings
from seven.compat.decorators import available_on


@available_on('1.4', '1.5')
def compat_function():
    pass


class TestAvailableOnDecorator(TestCase):

    @override_settings(CURRENT_DJANGO_VERSION='1.3')
    def test_current_django_version_is_not_supported(self):
        self.assertRaises(Exception, compat_function)
