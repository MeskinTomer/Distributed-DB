"""
The Python Class that implements the file-inputting database
"""

from DataBaseDict import DataBaseDict
import pickle
import os

FILE_PATH = 'data.pkl'


class DataBaseFile(DataBaseDict):
    def __init__(self):
        super().__init__()
        if not os.path.exists(FILE_PATH):
            self.file = open(FILE_PATH, 'wb')
        try:
            pickle.dump(self.dict, self.file)
        except Exception as error:
            print('Error - ' + str(error))

    def set_value(self, key, val):
        try:
            self.dict = pickle.load(self.file)
            super().set_value(key, val)
            pickle.dump(self.dict, self.file)
        except Exception as error:
            print('Error - ' + str(error))

    def get_value(self, key):
        try:
            self.dict = pickle.load(self.file)
            value = super().get_value(key)
            pickle.dump(self.dict, self.file)

            return value
        except Exception as error:
            print('Error - ' + str(error))

    def delete_value(self, key):
        try:
            self.dict = pickle.load(self.file)
            value = super().delete_value(key)
            pickle.dump(self.dict, self.file)

            return value
        except Exception as error:
            print('Error - ' + str(error))
