"""
The Python Class that implements the file-inputting database
"""

from DataBaseDict import DataBaseDict
import pickle
import os

FILE_PATH = 'data.pkl'


class DataBaseFile(DataBaseDict):
    def __init__(self, dictionary=None):
        # Initialize with the provided dictionary or an empty one
        super().__init__(dictionary or {})

        # Open the file in write-binary mode to replace its contents with the provided dictionary
        self.file = open(FILE_PATH, 'wb')

        # Immediately dump the provided dictionary to the file
        try:
            pickle.dump(self.dict, self.file)
            self.file.flush()  # Ensure that the data is written to the file
        except Exception as error:
            print('Error writing to file:', error)
        finally:
            self.file.close()  # Close the file after writing

        # Reopen the file in read-binary and write-binary mode for further operations
        self.file = open(FILE_PATH, 'r+b')

    def set_value(self, key, val):
        """Set a value in the dictionary, loading from the file each time."""
        try:
            self.file.seek(0)  # Ensure you're at the beginning of the file
            self.dict = pickle.load(self.file)  # Load existing data

            # Set the value in the dictionary
            super().set_value(key, val)

            # Write the updated dictionary back to the file
            self.file.seek(0)  # Go back to the beginning of the file to write
            self.file.truncate()  # Clear the file before writing
            pickle.dump(self.dict, self.file)
        except EOFError:
            print('File is empty or corrupted; initializing with an empty dictionary.')
            self.dict = {}
            super().set_value(key, val)
            self.file.seek(0)
            self.file.truncate()
            pickle.dump(self.dict, self.file)
        except Exception as error:
            print('Error - ' + str(error))

    def get_value(self, key):
        """Get a value from the dictionary, loading from the file each time."""
        try:
            self.file.seek(0)  # Ensure you're at the beginning of the file
            self.dict = pickle.load(self.file)  # Load existing data

            # Return the value for the given key, or None if the key doesn't exist
            return self.dict.get(key, None)
        except EOFError:
            print('File is empty or corrupted; cannot retrieve value.')
            return None
        except Exception as error:
            print('Error - ' + str(error))
            return None

    def delete_value(self, key):
        """Delete a key-value pair from the dictionary and save to the file."""
        try:
            self.file.seek(0)  # Ensure you're at the beginning of the file
            self.dict = pickle.load(self.file)  # Load existing data
            if key in self.dict:
                super().delete_value(key)
                self.file.seek(0)
                self.file.truncate()
                pickle.dump(self.dict, self.file)
            else:
                print(f"Key '{key}' not found.")
        except EOFError:
            print('File is empty or corrupted; cannot delete.')
        except Exception as error:
            print('Error - ' + str(error))
