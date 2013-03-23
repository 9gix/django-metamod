#!/usr/bin/env python
import os
import sys

FILE_DIR = os.path.dirname(__file__)
path = os.path.join(FILE_DIR, '..')
sys.path.insert(0, path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examples.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
