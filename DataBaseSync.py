"""
The Python Class that implements the synchronized database
"""

from DataBaseFile import DataBaseFile
import threading
import multiprocessing

MAX_READERS_COUNT = 10


class DataBaseSync(DataBaseFile):
    def __init__(self, mode):
        super().__init__()
        if mode == 'Threading':
            self.lock = threading.Lock()
            self.semaphore = threading.Semaphore(MAX_READERS_COUNT)
        elif mode == 'Multiprocessing':
            self.lock = multiprocessing.Lock
            self.semaphore = multiprocessing.Semaphore(MAX_READERS_COUNT)

    def set_value(self, key, val):
        with self.lock:
            permits_acquired = 0

            # Acquire all permits
            while permits_acquired < MAX_READERS_COUNT:
                self.semaphore.acquire()
                permits_acquired += 1
            print('All reading permits acquired')

            super().set_value(key, val)

        # Release all permits
        while permits_acquired > 0:
            self.semaphore.relese()
            permits_acquired -= 1

    def get_value(self, key):
        with self.semaphore:
            value = super().get_value(key)
        return value

    def delete_value(self, key):
        with self.lock:
            permits_acquired = 0

            # Acquire all permits
            while permits_acquired < MAX_READERS_COUNT:
                self.semaphore.acquire()
                permits_acquired += 1
            print('All reading permits acquired')

            value = super().delete_value(key)

        # Release all permits
        while permits_acquired > 0:
            self.semaphore.relese()
            permits_acquired -= 1

        return value
