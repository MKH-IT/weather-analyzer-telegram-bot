import json
import logging
from abc import ABC, abstractmethod
from pathlib import Path


class DatabaseBase(ABC):
    @abstractmethod
    def create_database(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def read(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def write(self, *args, **kwargs):
        raise NotImplementedError


class JSONDatabase(DatabaseBase):
    _FILE_PATH = "database.json"

    def __init__(self):
        self.create_database()

    def create_database(self):
        try:
            Path(self._FILE_PATH).touch()  # TODO: Add {} to the file while creating it.
            logging.info(f"File '{self._FILE_PATH}' created successfully!")
        except IOError:
            logging.error(f"Unable to create file '{self._FILE_PATH}'")
        return self

    def read(self) -> dict:
        with open(self._FILE_PATH, "r") as file:
            data = json.load(file)
        return data

    def write(self, data) -> None:
        with open(self._FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

    def read_all(self):
        with open(self._FILE_PATH, "r") as file:
            return file.read()


test_obj = JSONDatabase()
print(test_obj.read())
