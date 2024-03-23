import logging
from abc import ABC
from pathlib import Path


class DatabaseBase(ABC):
    pass


class JSONDatabase(DatabaseBase):
    FILE_PATH = "database.json"

    def __init__(self):
        try:
            Path(self.FILE_PATH).touch()
            logging.info(f"File '{self.FILE_PATH}' created successfully!")
        except IOError:
            logging.error(f"Unable to create file '{self.FILE_PATH}'")


class Database:
    def __init__(self, database: DatabaseBase):
        self.database = database
