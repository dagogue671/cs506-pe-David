"""
Problem 2: Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1: Input: s = "anagram", t = "nagaram" Output: true
Example 2: Input: s = "rat", t = "car" Output: false
Note: You may assume the string contains only lowercase alphabets.
Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such
case?
"""

def anagram(s,t):

    return_value = True

    for i in t:
        if i not in s:
            return_value = False
            break
    
    return return_value
