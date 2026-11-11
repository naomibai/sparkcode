"""Copy this into the WSGI configuration file in PythonAnywhere's Web tab.

Upload/clone this project into ~/sparkcopy, or update PROJECT_DIR below.
"""
import os
import sys

PROJECT_DIR = os.path.expanduser("~/sparkcopy")
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from app import app as application
