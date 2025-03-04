import os
import re
from datetime import datetime

def is_version_format(some_value: str) -> bool:
    pattern = r'^\d+\.\d+\.\d+$'
    return re.match(pattern, version)

def what_update(type_of_update: str, some_version: str) -> str:
    parts = some_version.split('.')
    if type_of_update == 'major':
        parts[0] = str(int(parts[0]) + 1)
        parts[1] = str(0)
        parts[2] = str(0)
    elif type_of_update == 'minor':
        parts[1] = str(int(parts[1]) + 1)
        parts[2] = str(0)
    elif type_of_update == 'patch':
        parts[2] = str(int(parts[2]) + 1)

    newest_value = '.'.join(parts)

    with open('version', 'w') as file:
        file.write(newest_value)

    return newest_value

if not os.path.exists('version'):
    with open('version', 'w') as file:
        file.write('1.0.0')
else:
    with open('version', 'r') as file:
        version = file.read()

update_type = input('Enter type of update (major, minor, patch): ')

if is_version_format(version):
    new_version = what_update(update_type, version)
else:
    with open('version', 'w') as file:
        file.write('1.0.0')
    with open('version', 'r') as file:
        version = file.read()
        new_version = what_update(update_type, version)

with open('version_log', 'a') as file:
    file.write('[' + new_version + ']' + ' <-- ' + '[' + version + ']' + ' [' + str(datetime.now()) + '] ' + update_type + ' update\n')