import os
import shutil
from .important import *

def get_file_names():
    file_names = [
        'config/whitelist-request.txt',
        'config/frontend-domains.txt'
    ]

    return file_names

def default_settings():
    for file_name in get_file_names():
        try:
            open(real_path('/../' + file_name))
        except FileNotFoundError:
            shutil.copyfile(real_path('/default/' + file_name), real_path('/../' + file_name))

def reset_to_default_settings():
    for file_name in get_file_names():
        try:
            os.remove(real_path('/../' + file_name))
        except FileNotFoundError: pass

    default_settings()
