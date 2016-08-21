
from django.db import models


class SuperHero(models.Model):
    name = models.CharField(max_length=255)


class SuperForeignKeyModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False


class SuperM2MModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False


class SuperModel(models.Model):
    non_related_field = models.CharField(max_length=255)
    foreign_key_field = models.ManyToManyField(SuperForeignKeyModel)
    m2m_field = models.ManyToManyField(SuperM2MModel)

    class Meta:
        managed = False


class SuperRelatedToSuperModel(models.Model):
    foreign_key_field = models.ForeignKey(SuperModel)

    class Meta:
        managed = False


class SuperRelated2ToSuperModel(models.Model):
    m2m_field = models.ManyToManyField(SuperModel)

    class Meta:
        managed = False
