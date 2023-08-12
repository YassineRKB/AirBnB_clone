#!/usr/bin/python3
"""storage engine initiator & classes preparation module"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
