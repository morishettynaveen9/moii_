import unittest
from main import count_objects

class TestMain(unittest.TestCase):
    def test_count_objects(self):
        boxes = [{'x': 10, 'y': 20, 'w': 30, 'h': 40}, {'x': 50, 'y': 60, 'w': 70, 'h': 80}]
        result = count_objects(boxes)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
