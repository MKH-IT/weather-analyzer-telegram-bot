import logging
from abc import ABC, abstractmethod
from pathlib import Path


class DatabaseBase(ABC):
    @abstractmethod
    def create_database(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def read_all(self, *args, **kwargs):
        raise NotImplementedError


class JSONDatabase(DatabaseBase):
    _FILE_PATH = "database.json"

    def __init__(self):
        self.create_database()

    def create_database(self):
        try:
            Path(self._FILE_PATH).touch()
            logging.info(f"File '{self._FILE_PATH}' created successfully!")
        except IOError:
            logging.error(f"Unable to create file '{self._FILE_PATH}'")
        return self

    def read_all(self):
        with open(self._FILE_PATH, "r") as file:
            return file.read()
