============
Django Seven
============

.. image:: https://travis-ci.org/iwoca/django-seven.svg?branch=develop
    :target: https://travis-ci.org/iwoca/django-seven.svg

Collection of code/tools to help for Django upgrading.
This package name is a reference to python package 'six' which was helping compatibility between python 2 and 3.

The idea of this package is to share some experience gained from a Django upgrade from 1.4 to 1.9 on a quite big project.
Have a look at `Django Upgrade talk`_ for more details.
django-seven will at the beginning contain compat module and deprecated rules logic.


Deprecated rules
================

A Django management command  ``check_deprecated_rules`` is available to check if your project is "upgrade-compatible".
You should first add ``django_seven.deprecated_rules`` tou your ``INSTALLED_APPS``:


::

    INSTALLED_APPS = [
        ...
        'django_seven.deprecated_rules',
    ]


Then launch the management command for your project:

::

    $ ./manage.py check_deprecated_rules

    ./core/models.py
    1601: models.BooleanField has to be initialised with default parameter,
          as implicit default has changed between Django 1.4 (False) and 1.6 (None).
    L6:     boolean_field = models.BooleanField()


This command will give you a list of non-respected rules, with useful informations to fix them:
- The impacted file,
- The rule number, with an explanation of the rule,
- The line number, and the line copy.

[UNDER HEAVY DEVELOPMENT / DESIGN CHOICES]

.. _Django Upgrade talk: https://romgar.github.io/presentations/django_upgrade/
