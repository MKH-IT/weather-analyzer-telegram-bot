from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def choices(cls):
        return [e.value for e in cls]

    @classmethod
    def as_dict(cls):
        return {e.name: e.value for e in cls}

    def __get__(self, instance, owner):
        return self.value
