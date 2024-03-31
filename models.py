"""
Database architecture.
    User ID -> Language -> Location -> Phone Number -> Notification Time
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from database import DatabaseBase


@dataclass
class User:
    user_id: int
    language: str
    location: str
    phone_number: str
    notification_time: str


class UserRepositoryBase(ABC):
    @abstractmethod
    def create_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def get_all_users(self, user: User):
        raise NotImplementedError


class UserRepositoryJSONHandler(UserRepositoryBase):
    def __init__(self, database: DatabaseBase):
        self.database = database

    def create_user(self, user: User):
        pass

    def get_user(self, user: User):
        pass

    def update_user(self, user: User):
        pass

    def delete_user(self, user: User):
        pass

    def get_all_users(self, user: User):
        pass
