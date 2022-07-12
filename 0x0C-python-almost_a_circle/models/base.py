#!/usr/bin/python3
"""Module level comment"""


class Base:
    """Class documentation"""
    __nb_objects = 0

    def __init__(self, id=None):
        '''Function documentation'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__
        print(filename)
        if list_objs is None:
            content = []
        else:
            print(list_objs)
            # content = list_objs
        with open(filename, 'w') as f:
            f.write(Base.to_json_string(content))

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        pass
