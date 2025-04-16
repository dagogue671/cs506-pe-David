import unittest
from Problem1 import strStr
from Problem2 import anagram


class TestPE02(unittest.TestCase):


    def test_problem1(self):
        # Case 1: Paramater 2 is a substring of Parameter 1. Return 2
        self.assertEqual(strStr("hello","ll"), 2)

        # Case 2: Parameter 2 is not a substring of Paramter 1. Return -1
        self.assertEqual(strStr("aaaaa","bba"), -1)

        # Case 3: Parameter 2 is empty
        self.assertEqual(strStr("aaaaa",""), 0)

    def test_problem2(self):
        # Case 1: Parameter 2 is an anagram of Parameter 1
        self.assertTrue(anagram("anagram", "nagrama"))

        # Case 2: Parameter 2 is not an anagram of Parameter 1
        self.assertFalse(anagram("rat","car"))

if __name__=="__main__":
    unittest.main()