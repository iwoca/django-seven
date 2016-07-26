# Old Django transaction system
from django.db import transaction
from django.db.transaction import commit_on_success, commit_manually
from django.http import HttpResponse


@transaction.commit_on_success()
def view(request):
    return HttpResponse('Request in a transaction')


def view_with_context_manager(request):
    with commit_on_success():
        return HttpResponse('Request in a transaction')


class DummyClass(object):
    @commit_on_success()
    def method(request):
        return True


@transaction.commit_manually()
def view(request):
    return HttpResponse('Request in a transaction')


# New Django transaction system
@transaction.atomic()
def view(request):
    return HttpResponse('Request in a transaction')
