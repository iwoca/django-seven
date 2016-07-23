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

You should first add ``django_seven.deprecated_rules`` to your ``INSTALLED_APPS``:


::

    INSTALLED_APPS = [
        ...
        'django_seven.deprecated_rules',
    ]


Then you should define your current Django version and the version you want to upgrade to in your settings file:

::

    CURRENT_DJANGO_VERSION = '1.4'
    FUTURE_DJANGO_VERSION = '1.9'


Then launch the ``check_deprecated_rules`` management command for your project:

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

By default, ``django-seven`` is defining some deprecated rules, but you can also define yours in settings file.
You should respect the rule fields:

::

    DEPRECATED_RULES = [
        {
            'name': 'deprecated_django_local_flavor_module',
            'message': 'Deprecated django.contrib.localflavor module (now third-party lib). Use localflavor instead.',
            'regex': r'.*django\.contrib\.localflavor.*',
            'number': '1602',
            'should_be_fixed_in': '1.6',
        },
    ]

You can also use the ``django-seven`` ones and add yours:

::

    CUSTOM_RULES = [
        # Your custom rules
    ]

    from django_seven.deprecated_rules.rules import DEPRECATED_RULES as SV_DEPRECATED_RULES
    DEPRECATED_RULES = SV_DEPRECATED_RULES + CUSTOM_RULES


You can specify through settings which directories/files you want to exclude from the deprecated rules search:

::

    SEVEN_EXCLUDED_DIRS = ['venv', '.git', 'frontend', 'static', 'docs']
    SEVEN_EXCLUDED_SUB_PATHS = ['migrations']
    SEVEN_EXCLUDED_SPECIFIC_FILE = ['my/specific/file.py']
    SEVEN_EXCLUDED_FILE_EXTENSIONS = ['.pyc']


[UNDER HEAVY DEVELOPMENT / DESIGN CHOICES]

.. _Django Upgrade talk: https://romgar.github.io/presentations/django_upgrade/
