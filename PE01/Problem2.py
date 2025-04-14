"""
Problem 2: Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit

Example:
Input: 38 Output:2
3 + 8 = 11 => 1 + 1 = 2

Follow up: 
Could you do it without any loop/recursion?
"""


non_negative_num = int(input("Please enter a non-negative number: ")) # Input saved as a string
temp = 0

while non_negative_num >= 10:
    temp += non_negative_num % 10
