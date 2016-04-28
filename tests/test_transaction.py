
from django.test import TransactionTestCase

from seven.compat.db import transaction
from tests.models import SuperHero


class AtomicTransactionTest(TransactionTestCase):

    def test_decorator_compat_for_rollback(self):

        @transaction.atomic_compat_transaction
        def create_user():
            SuperHero.objects.create('Wolverine')
            raise Exception("Rollback should happen")

        with self.assertRaises(Exception):
            create_user()

        self.assertQuerysetEqual(SuperHero.objects.all(), [])

    def test_context_manager_compat_for_rollback(self):

        with self.assertRaises(Exception):
            with transaction.atomic_compat_transaction():
                SuperHero.objects.create_user('johndoe')
                raise Exception("Rollback should happen")

        self.assertQuerysetEqual(SuperHero.objects.all(), [])
