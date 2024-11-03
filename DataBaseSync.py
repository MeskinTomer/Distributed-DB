"""
The Python Class that implements the synchronized database
"""
import time

from DataBaseFile import DataBaseFile
import threading
import multiprocessing

MAX_READERS_COUNT = 10


class DataBaseSync(DataBaseFile):
    def __init__(self, dictionary=None, mode='Threading'):
        super().__init__(dictionary)
        if dictionary is None:
            dictionary = {}
        if mode == 'Threading':
            self.lock = threading.Lock()
            self.semaphore = threading.Semaphore(MAX_READERS_COUNT)
        elif mode == 'Multiprocessing':
            self.lock = multiprocessing.Lock()
            self.semaphore = multiprocessing.Semaphore(MAX_READERS_COUNT)

    def set_value(self, key, val):
        with self.lock:
            permits_acquired = 0

            # Acquire all permits
            while permits_acquired < MAX_READERS_COUNT:
                self.semaphore.acquire()
                permits_acquired += 1

            super().set_value(key, val)
            print(f'Set - {key}: {val}')
            time.sleep(3)

        # Release all permits
        while permits_acquired > 0:
            self.semaphore.release()
            permits_acquired -= 1

    def get_value(self, key):
        with self.semaphore:
            value = super().get_value(key)
            print(f'Read - {key}: {value}')
            time.sleep(3)
        return value

    def delete_value(self, key):
        with self.lock:
            permits_acquired = 0

            # Acquire all permits
            while permits_acquired < MAX_READERS_COUNT:
                self.semaphore.acquire()
                permits_acquired += 1

            value = super().delete_value(key)
            print(f'Deleted - {key}: {value}')
            time.sleep(3)

        # Release all permits
        while permits_acquired > 0:
            self.semaphore.release()
            permits_acquired -= 1

        return value

    def __str__(self):
        return str(self.dict)
