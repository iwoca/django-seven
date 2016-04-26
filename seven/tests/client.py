import mock

import django
from django.test.client import ClientHandler, Client


class MyClientHandler(ClientHandler):
    # While PatchedClient calls its base class the django.test.client.ClientHandler is patched
    # to MyClientHandler. For this reason ClientHandler.__init__ would get into an infinite
    # recursion while calling its base class __init__ (because super(django.test.client.ClientHandler, self)
    # would evaluate to ClientHandler instead of the ClientHandler base class).
    @mock.patch('django.test.client.ClientHandler', ClientHandler)
    def __init__(self, *args, **kwargs):
        super(MyClientHandler, self).__init__(*args, **kwargs)

    def get_response(self, request):
        response = super(MyClientHandler, self).get_response(request)
        response.wsgi_request = request
        return response


if django.VERSION < (1, 7):
    class PatchedClient(Client):
        """ FIXME: This is an unnecessary hack to have the response.wsgi_request attribute that
        is supported only in django 1.7+. After upgrading to django 1.7+ MyClientHandler can
        be deleted and you can start using Client instead of this PatchedClient. """
        def __init__(self, *args, **kwargs):
            assert django.VERSION[:2] < (1, 7), 'FIXME: remove this hack! (PatchedClient and MyClientHandler)'
            with mock.patch('django.test.client.ClientHandler', MyClientHandler):
                super(PatchedClient, self).__init__(*args, **kwargs)
else:
    PatchedClient = Client
