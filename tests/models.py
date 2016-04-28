
from django.db import models


class SuperHero(models.Model):
    name = models.CharField(max_length=255)
