#!/usr/bin/python3
"""Class Model"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class Base model that defines all
    common attributes/methods for other
    classes
    """

    def __init__(self, *args, **kwargs) -> None:
        """initialization of BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at, updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """set updated_at to now datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """returns the dictionary containing all keys/values"""
        ToDict = dict(self.__dict__)
        ToDict["__class__"] = self.__class__.__name__
        if not isinstance(ToDict["created_at"], str):
            ToDict["created_at"] = ToDict["created_at"].isoformat()
        if not isinstance(ToDict["updated_at"], str):
            ToDict["updated_at"] = ToDict["updated_at"].isoformat()
        return ToDict
