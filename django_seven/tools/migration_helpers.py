
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))
frozen_migrations_filename = '{current_path}/frozen_migrations_state.json'.format(current_path=current_path)


def filter_apps_to_migrate(apps_list, EXCLUDED_FROM_MIGRATIONS_CREATION):

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
