
from django.db import models


# Old query set method in managers...
class MyModelManager(models.Manager):

    def get_query_set(self):
        return super(MyModelManager, self).get_query_set()


# ...replaced by new one
class MyModelManager(models.Manager):

    def get_queryset(self):
        return super(MyModelManager, self).get_queryset()
