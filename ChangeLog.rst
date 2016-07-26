ChangeLog
=========


.. _v0.1.1:

0.1.1 (2016-07-26)
------------------

*New:*

    - Adding `SEVEN_CURRENT_DJANGO_VERSION` and `SEVEN_FUTURE_DJANGO_VERSION` settings to specify which version
      you are starting from and which version do you want to migrate to. That will allow `django-seven` to know
      which parts are relevant to be applied to your project,
    - Adding `SEVEN_EXCLUDED_DIRS`, `SEVEN_EXCLUDED_SUB_PATHS`, `SEVEN_EXCLUDED_SPECIFIC_FILE` and
      `SEVEN_EXCLUDED_FILE_EXTENSIONS` to specify which folders/files you want to exclude from your deprecated
      rules search,
    - Adding test coverage for all rules checked by `check_deprecated_rules` management command.


.. _v0.1:

0.1 (2016-07-20)
----------------

*New:*

    - Releasing `check_deprecated_rules` management command to check if all deprecated rules have been respected.
