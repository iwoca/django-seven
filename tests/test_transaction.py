from django.contrib.auth.models import User
from django.test import TransactionTestCase

from upgrade_tools.db import transaction


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


class CustomerManagedTransactionTest(TransactionTestCase):

    def test_that_managed_transaction_does_not_swallow_exceptions_if_code_error(self):
        """
        It's quite surprising, as commit_on_success usually raises the Exception.
        It seems that, in some situations, the rollback was done without any Exception raised.
        This managed_transaction is more a gatekeeper, and will disappear with new atomic transaction management.
        """
        @transaction.managed_transaction
        def create_user():
            User.objects.create_user('johndoe')
            raise Exception("Rollback should happen")

        with self.assertRaises(Exception):
            create_user()
