from django.db import models


class SuperHero(models.Model):
    bad_boolean_field = models.BooleanField()
    good_boolean_field = models.BooleanField(default=False)
