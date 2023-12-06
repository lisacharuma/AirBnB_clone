#!/usr/bin/python3
from os.path import exists
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    infomation = json.load(file)

                    for key, obj in infomation.items():
                        class_name, obj_id = key.split('.')
                        obj_class = eval(class_name)
                        obj_instance = obj_class(**obj)
                        self.__objects[key] = obj_instance
                except Exception:
                    pass
