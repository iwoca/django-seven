from django.test import TestCase

from django_seven.compat.models import meta as compat_meta
from tests.models import SuperModel


class TestModelMetaMethods(TestCase):

    def test_get_fields_with_model(self):
        self.assertEqual(compat_meta.get_fields_with_model(SuperModel), [])

    def get_concrete_fields_with_model(self):
        self.assertEqual(compat_meta.get_concrete_fields_with_model(SuperModel), [])

    def get_m2m_with_model(self):
        self.assertEqual(compat_meta.get_m2m_with_model(SuperModel), [])

    def get_all_related_objects(self):
        self.assertEqual(compat_meta.get_all_related_objects(SuperModel), [])

    def get_all_related_objects_with_model(self):
        self.assertEqual(compat_meta.get_all_related_objects_with_model(SuperModel), [])

    def get_all_related_many_to_many_objects(self):
        self.assertEqual(compat_meta.get_all_related_many_to_many_objects(SuperModel), [])

    def get_all_related_m2m_objects_with_model(self):
        self.assertEqual(compat_meta.get_all_related_m2m_objects_with_model(SuperModel), [])

    def get_all_field_names(self):
        self.assertEqual(compat_meta.get_all_field_names(SuperModel), [])
