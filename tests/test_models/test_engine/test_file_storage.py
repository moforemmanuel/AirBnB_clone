import unittest
from models.engine.file_storage import FileStorage


class MyTestCase(unittest.TestCase):
    """
    File Storage test class
    """
    def test_instantiation(self):
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)


if __name__ == '__main__':
    unittest.main()
