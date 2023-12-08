#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""BaseModel module"""


class BaseModel:
    """Reprsents BaseModel instances"""
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel"""
        class_name = None
        if kwargs:
            """class_name = kwargs.pop("__class__", None)"""
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        """if class_name:
            setattr(self, "__class__", class_name)"""

    def __str__(self):
        """Defines string rep for instances"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Saves instances"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """convert instances to dict"""
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()

        return object_dict
