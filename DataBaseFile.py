import pickle
import os
from DataBaseDict import DataBaseDict

FILE_PATH = 'data.pkl'


class DataBaseFile(DataBaseDict):
    def __init__(self, dictionary=None):
        """Initialize with the provided dictionary, saving it to a file."""
        # Initialize with the provided dictionary or an empty one
        super().__init__(dictionary or {})
        self._save_to_file()  # Save initial dictionary to file

    def _save_to_file(self):
        """Helper method to save the current dictionary to file."""
        with open(FILE_PATH, 'wb') as file:
            pickle.dump(self.dict, file)

    def _load_from_file(self):
        """Helper method to load the dictionary from file."""
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'rb') as file:
                self.dict = pickle.load(file)
        else:
            self.dict = {}

    def set_value(self, key, val):
        """Set a value in the dictionary and save to file."""
        self._load_from_file()  # Load current data
        super().set_value(key, val)  # Use the parent class method
        self._save_to_file()  # Save updated data

    def get_value(self, key):
        """Get a value from the dictionary, loading from the file each time."""
        self._load_from_file()
        return super().get_value(key)  # Use the parent class method

    def delete_value(self, key):
        """Delete a key-value pair from the dictionary and save to the file."""
        self._load_from_file()
        super().delete_value(key)  # Use the parent class method
        self._save_to_file()
