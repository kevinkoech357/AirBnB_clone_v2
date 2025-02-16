#!/usr/bin/python3

"""
This module instantiates an object of class FileStorage
"""


from models.engine.file_storage import FileStorage
from os import getenv


# Condition depending of the value of the
# environment variable HBNB_TYPE_STORAGE
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
