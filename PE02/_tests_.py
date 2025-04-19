import unittest
from Problem1 import strStr
from Problem2 import anagram
from Problem3 import longest_common_prefix as lcp


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

    def test_problem3(self):
        list1 = ["flower", "flow", "flight"]
        list2 = ["dog","racecar", "car"]
        list3 = ["apple","appricot","apple","appalachian","apps"]

        # Test List 1
        self.assertEqual(lcp(list1), "fl")

        # Test List 2
        self.assertEqual(lcp(list2), "")

        # Test List 3
        self.assertEqual(lcp(list3), "app")
    
    def test_problem4(self):
        print("Problem 4 is created as a set up for user input.")
        print("Please run Problem 4 through your command line or terminal.")

    

if __name__=="__main__":
    unittest.main()