from itertools import chain

import django

"""
All these functions have been copied from Django documentation
https://docs.djangoproject.com/en/1.10/ref/models/meta/
"""


def get_field(model_class, name):
    if django.VERSION < (1, 9):
        return model_class._meta.get_field(name)
    else:
        f = model_class._meta.get_field(name)
        if f.auto_created is False and f.is_relation and f.related_model is None:
            return f


def get_field_by_name(model_class, name):
    if django.VERSION < (1, 9):
        return model_class._meta.get_field_by_name(name)
    else:
        field = model_class._meta.get_field(name)
        model = field.model
        direct = not field.auto_created or field.concrete
        m2m = field.many_to_many
        return field, model, direct, m2m


def get_fields_with_model(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_fields_with_model()
    else:
        return [
            (f, f.model if f.model != model_class else None)
            for f in model_class._meta.get_fields()
            if not f.is_relation
            or f.one_to_one
            or (f.many_to_one and f.related_model)
        ]


def get_concrete_fields_with_model(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_concrete_fields_with_model()
    else:
        return [
            (f, f.model if f.model != model_class else None)
            for f in model_class._meta.get_fields()
            if f.concrete and (
                not f.is_relation
                or f.one_to_one
                or (f.many_to_one and f.related_model)
            )
        ]


def get_m2m_with_model(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_m2m_with_model()
    else:
        return [
            (f, f.model if f.model != model_class else None)
            for f in model_class._meta.get_fields()
            if f.many_to_many and not f.auto_created
        ]


def get_all_related_objects(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_all_related_objects()
    else:
        return [
            f for f in model_class._meta.get_fields()
            if (f.one_to_many or f.one_to_one)
            and f.auto_created and not f.concrete
        ]


def get_all_related_objects_with_model(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_all_related_objects_with_model()
    else:
        return [
            (f, f.model if f.model != model_class else None)
            for f in model_class._meta.get_fields()
            if (f.one_to_many or f.one_to_one)
            and f.auto_created and not f.concrete
        ]


def get_all_related_many_to_many_objects(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_all_related_many_to_many_objects()
    else:
        return [
            f for f in model_class._meta.get_fields(include_hidden=True)
            if f.many_to_many and f.auto_created
        ]


def get_all_related_m2m_objects_with_model(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_all_related_m2m_objects_with_model()
    else:
        return [
            (f, f.model if f.model != model_class else None)
            for f in model_class._meta.get_fields(include_hidden=True)
            if f.many_to_many and f.auto_created
        ]


def get_all_field_names(model_class):
    if django.VERSION < (1, 9):
        return model_class._meta.get_all_field_names()
    else:
        return list(set(chain.from_iterable(
            (field.name, field.attname) if hasattr(field, 'attname') else (field.name,)
            for field in model_class._meta.get_fields()
            # For complete backwards compatibility, you may want to exclude
            # GenericForeignKey from the results.
            if not (field.many_to_one and field.related_model is None)
        )))
