from django.contrib.auth.models import User
from django.test import TransactionTestCase
from seven.compat.db import transaction


class AtomicTransactionTest(TransactionTestCase):

    def test_decorator_compat_for_rollback(self):

        @transaction.atomic_compat_transaction
        def create_user():
            User.objects.create_user('johndoe')
            raise Exception("Rollback should happen")

        with self.assertRaises(Exception):
            create_user()

        self.assertQuerysetEqual(User.objects.all(), [])

    def test_context_manager_compat_for_rollback(self):

        with self.assertRaises(Exception):
            with transaction.atomic_compat_transaction():
                User.objects.create_user('johndoe')
                raise Exception("Rollback should happen")

        self.assertQuerysetEqual(User.objects.all(), [])
