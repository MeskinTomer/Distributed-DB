"""
The Python Class that implements the base database
"""


class DataBaseDict:
    def __init__(self):
        self.dict = {}

    def set_value(self, key, val):
        self.dict[key] = val

    def get_value(self, key):
        return self.dict.get(key, None)

    def delete_value(self, key):
        self.dict.pop(key, None)