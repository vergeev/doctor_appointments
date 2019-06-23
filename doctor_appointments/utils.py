from enum import Enum


class ChoicesEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple((choice.name, choice.value) for choice in cls)
