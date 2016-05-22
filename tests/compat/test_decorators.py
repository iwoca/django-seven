from django.test import TestCase
from django.test.utils import override_settings
from django_seven.compat.decorators import available_on


@available_on('1.4', '1.8')
def compat_function():
    pass


class TestAvailableOnDecorator(TestCase):

    @override_settings(CURRENT_DJANGO_VERSION='1.3', FUTURE_DJANGO_VERSION='1.5')
    def test_current_django_version_is_too_old(self):
        self.assertRaises(Exception, compat_function)

    @override_settings(CURRENT_DJANGO_VERSION='1.9', FUTURE_DJANGO_VERSION='1.10')
    def test_current_django_version_is_too_recent(self):
        self.assertRaises(Exception, compat_function)

    @override_settings(CURRENT_DJANGO_VERSION='1.8.1', FUTURE_DJANGO_VERSION='1.10')
    def test_current_django_minor_version_is_too_recent(self):
        self.assertRaises(Exception, compat_function)

    @override_settings(CURRENT_DJANGO_VERSION='1.2', FUTURE_DJANGO_VERSION='1.3')
    def test_future_django_version_is_too_old(self):
        self.assertRaises(Exception, compat_function)

    @override_settings(CURRENT_DJANGO_VERSION='1.5', FUTURE_DJANGO_VERSION='1.10')
    def test_future_django_version_is_too_recent(self):
        self.assertRaises(Exception, compat_function)

    @override_settings(CURRENT_DJANGO_VERSION='1.4.1', FUTURE_DJANGO_VERSION='1.7.10')
    def test_correct_versions(self):
        compat_function()
