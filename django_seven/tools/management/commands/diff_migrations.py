from __future__ import absolute_import

from optparse import make_option
import pprint

from django.core.management.base import BaseCommand
from django.conf import settings
from seven.tools.migration_helpers import filter_apps_to_migrate, get_filesystem_migrations, freeze_migrations, \
    frozen_migrations_filename, get_frozen_migrations, get_diff


EXCLUDED_FROM_MIGRATIONS_CREATION = []


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option(
            '--save',
            action='store_true',
            dest='freeze_migrations',
            default=False,
            help='If used, save current filesystem migrations in a file'
        ),
        make_option(
            '--dump',
            action='store_true',
            dest='dump_migrations',
            default=False,
            help='If used, dump current frozen migrations'
        ),
    )

    def handle(self, *args, **options):
        """ The idea is to freeze the migrations I have already processed in the new-style migration.
            If people are pushing new migrations, I will know, after saving what I already have managed,
            which ones I need to update.

            If the command is launched without arguments, I get the diff between actual migrations and the frozen ones
            With --save parameters, we save current migrations in the filesystem in a json file.
        """
        apps_to_init = filter_apps_to_migrate(settings.INSTALLED_APPS)

        if 'freeze_migrations' in options and options['freeze_migrations']:
            current_migrations = get_filesystem_migrations(apps_to_init, EXCLUDED_FROM_MIGRATIONS_CREATION)
            freeze_migrations(current_migrations)
            pprint.pprint(current_migrations)
            print 'Migrations saved in {filename}'.format(filename=frozen_migrations_filename)
        elif 'dump_migrations' in options and options['dump_migrations']:
            frozen_migrations = get_frozen_migrations()
            pprint.pprint(frozen_migrations)
        else:
            current_migrations = get_filesystem_migrations(apps_to_init)
            frozen_migrations = get_frozen_migrations()

            migrations_diff = get_diff(current_migrations, frozen_migrations)
            if migrations_diff:
                print 'Migrations diff:'
                pprint.pprint(migrations_diff)
            else:
                print 'No differences found'
