import unittest
from IsPolindrome import isPolindrome
from InvertArray import invertArray
from IsPolindrome import isPolindrome
from RomanNumbers import romanToInt
class TestArrays(unittest.TestCase):
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

    def test_isPolindrome(self):
        pass
      #  self.assertTrue(isPolindrome(['a', 'r', 'a']))
      #  self.assertFalse(isPolindrome(['a', 'r', 'm', 'a', 'n']))

    def test_romanToInt(self):
        self.assertEqual(romanToInt("MCMXCIV"), 1994)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("III"), 3)

if __name__ == '__main__':
    unittest.main()


