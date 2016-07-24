
from django.db import transaction
from django.http import HttpResponse


# Old HttpResponse mimetype parameter
def view(request):
    return HttpResponse(mimetype='application/json')


# New HttpResponse content_type parameter
@transaction.atomic()
def view(request):
    return HttpResponse(content_type='application/json')
