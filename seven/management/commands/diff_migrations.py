from __future__ import absolute_import
import json
from optparse import make_option
import os
import pprint

from django.core.management.base import BaseCommand
from django.conf import settings


current_path = os.path.dirname(os.path.abspath(__file__))
frozen_migrations_filename = '{current_path}/frozen_migrations_state.json'.format(current_path=current_path)


EXCLUDED_FROM_MIGRATIONS_CREATION

def filter_apps_to_migrate(apps_list):

    # We replace '.' to '/' to also get the right path for sub-apps.
    return [app_name.replace('.', '/') for app_name in apps_list if app_name not in EXCLUDED_FROM_MIGRATIONS_CREATION]


def get_filesystem_migrations(app_list):
    current_migrations = {}

    for app in app_list:
        try:
            current_migrations[app] = [filename for filename in os.listdir(app + '/south_migrations/')
                                       if not filename.endswith('.pyc') and filename.startswith('0')]
        except OSError:
            pass

    return current_migrations


def get_frozen_migrations():
    try:
        with open(frozen_migrations_filename) as migration_data:
            return json.loads(migration_data.read())
    except IOError:
        return {}


def freeze_migrations(migrations):
    with open(frozen_migrations_filename, "w") as migration_data:
        migration_data.write(json.dumps(migrations))


def get_diff(current, old):

    diff = {}

    keys_diff = list(set(current.keys()) - set(old.keys()))

    for key in keys_diff:
        diff[key] = current[key]

    for current_key, current_value in current.iteritems():
        if current_key in keys_diff:
            diff[current_key] = current_value
        else:
            migration_file_diff = sorted(list(set(current_value) - set(old[current_key])))
            if migration_file_diff:
                diff[current_key] = migration_file_diff
    return diff


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--save',
            action='store_true',
            dest='freeze_migrations',
            default=False,
            help='If used, save current filesystem migrations in a file'
        ),
        make_option('--dump',
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
            current_migrations = get_filesystem_migrations(apps_to_init)
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
