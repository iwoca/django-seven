=================
Django Modernizer
=================


Project introduction
====================
This project aims to fill a gap in our way to upgrade our Django projects.

The objective is **NOT** to create a tool that will handle the whole upgrade for the project (that's literally impossible).
The objective is to help making this upgrade process easier and faster by handling what can be automated.

It would be a 2to3 for Django, or even better, a `python-modernize`_


Motivation
==========
Working in a company with a quite big Django project (100+ apps, 400+ models, ...), I had to handle
an upgrade from a deprecated Django 1.4 to a newly released Django 1.8.
But when you have a big project with a lot of people working on it (20+ people), it's quite hard
to execute this upgrade seamless.

This is specially due to the fact that, while you will work to upgrade your project, other developers
will still continue to create deprecated code at the meantime.

At that point, I decided to create a code compatible with Django 1.4 **AND** Django 1.8, and
some deprecated rules to prevent my colleagues to write deprecated code.
I created a presentation to explain this approach: `django upgrade process`_
That worked very well, almost no regression during the whole process, and we finally got our
project compatible with both old and new version.

A talk this year at DjangoUnderTheHood from Carl Meyer showed that Instagram used the same approach
to upgrade their Django project.


The goal
========
The idea is to create a tool parsing a whole Django project to detect and fix anything useful to
help on a Django upgrade.

It would then depend on the nature of the fix.

A first interesting step would be to identify all types of backward incompatibility in Django
upgrades to define the possibly automated ones.






.. _python-modernize: https://github.com/mitsuhiko/python-modernize
.. _django upgrade process: http://romgar.github.io/presentations/django_upgrade/#/