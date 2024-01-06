import unittest
from functions import cube

class TestCube(unittest.TestCase):
    def test_cube(self):
        result = cube(2)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()