from functools import wraps
import django
from django.db import transaction

if django.VERSION < (1, 6):
    atomic_compat_transaction = transaction.commit_on_success
else:
    atomic_compat_transaction = transaction.atomic


if django.VERSION < (1, 6):
    def managed_transaction(func):
        """ This decorator wraps a function so that all sql executions in the function are atomic

            It's used instead of django.db.transaction.commit_on_success in cases where reporting exceptions is necessary
            as commit_on_success swallows exceptions
        """
        @wraps(func)
        @transaction.commit_manually
        def _inner(*args, **kwargs):
            try:
                ret = func(*args, **kwargs)
            except Exception:
                transaction.rollback()
                raise
            else:
                transaction.commit()
                return ret

        return _inner
else:
    """ transaction.atomic is the successor of commit_on_success, and not swallows exceptions anymore.
        we can then get rid of that hack for django 1.6+
    """
    managed_transaction = transaction.atomic
