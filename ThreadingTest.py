"""
The Python Class that implements the testing of the database using Threading
"""

import threading
import multiprocessing
from DataBaseSync import DataBaseSync


class ThreadingTest:
    def __init__(self):
        self.threads = []
        self.data_base = DataBaseSync()

    def test_1(self):
        self.data_base.set_value('test 1', 'complete')

    def test_2(self):
        return self.data_base.get_value('test 2')

    def test_3(self):
        thread = threading.Thread(target=self.data_base.get_value, args=('test 3',))
        thread.start()
        self.threads.append(thread)

        thread = threading.Thread(target=self.data_base.set_value, args=('test 3', 'complete'))
        thread.start()
        self.threads.append(thread)

        for thread in self.threads:
            thread.join()

    def test_4(self):
        thread = threading.Thread(target=self.data_base.set_value, args=('test 4', 'complete'))
        thread.start()
        self.threads.append(thread)

        thread = threading.Thread(target=self.data_base.get_value, args=('test 4',))
        thread.start()
        self.threads.append(thread)

        for thread in self.threads:
            thread.join()

    def test_5(self):
        for num in range(1, 6):
            thread = threading.Thread(target=self.data_base.get_value, args=('test 5',))
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()

    def test_6(self):
        for num in range(1, 6):
            thread = threading.Thread(target=self.data_base.get_value, args=('test 6',))
            thread.start()
            self.threads.append(thread)

        thread = threading.Thread(target=self.data_base.set_value, args=('test 6', 'complete 1'))
        self.threads.append(thread)

        thread = threading.Thread(target=self.data_base.set_value, args=('test 6', 'complete 2'))
        self.threads.append(thread)

        for thread in self.threads:
            thread.join()

    def test_all(self):
        self.test_1()
        self.test_2()
        self.test_3()
        self.test_4()
        self.test_5()
        self.test_6()


if __name__ == '__main__':
    test = ThreadingTest()
    test.test_4()
