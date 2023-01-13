import unittest
from InvertArray import invertArray
class TestStringMethods(unittest.TestCase):
    def test_invertArray(self):
        arr = []
        invertArray(arr)
        self.assertEqual(arr, [])
        arr = ['a']
        invertArray(arr)
        self.assertEqual(arr, ['a'])
        arr = ['a', 'b']
        invertArray(arr)
        self.assertEqual(arr, ['b', 'a'])
        arr = ['a', 'r', 'm', 'a', 'n']
        invertArray(arr)
        self.assertEqual(arr, ['n', 'a', 'm', 'r', 'a'])

if __name__ == '__main__':
    unittest.main()


