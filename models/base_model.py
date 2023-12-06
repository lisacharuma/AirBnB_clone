#!/usr/bin/python3
import uuid
from models import storage
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            class_name = kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
        if class_name:
            setattr(self, "__class__", class_name)

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        storage.save()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()

        return object_dict
