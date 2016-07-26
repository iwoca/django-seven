from django.http import HttpResponse


# Old request raw_post_data attribute
def view(request):
    request_payload = request.raw_post_data
    return HttpResponse('Old raw post data')


# New request body attribute
def view(request):
    request_payload = request.body
    return HttpResponse('New request body attribute')
