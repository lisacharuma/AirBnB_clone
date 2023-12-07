#!/usr/bin/python3
from os.path import exists
import json


class FileStorage:
    """

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """

        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Saves new BaseModel objs to FileStorage dict
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes obj to JSON file
        """
        serialized_objects = {}
        for obj in FileStorage.__objects.keys():
            serialized_objects[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes JSON file to objs
        """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    serialized_objects = json.load(file)

                    for key, obj in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        obj_class = eval(class_name)
                        obj_instance = obj_class(**obj)
                        FileStorage.__objects[key] = obj_instance
                except Exception:
                    pass
