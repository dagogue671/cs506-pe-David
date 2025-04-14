"""
Problem 2: Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit

Example:
Input: 38 Output:2
3 + 8 = 11 => 1 + 1 = 2

Follow up: 
Could you do it without any loop/recursion?

Answer: You could use sets to add the sum of a set of numbers as long as the total sum of the 
is less than 10
"""


non_negative_num = int(input("Please enter a non-negative number: ")) # Input as string then cast as int

while non_negative_num >= 10:
    
    sum_of_digits = 0 
    
    # work from the the one's place to the nth place until non_negative_num //= 10 equals 0
    while non_negative_num > 0:
        sum_of_digits += non_negative_num % 10 # Add one's place to the sum_of_digits
        non_negative_num //= 10 # add the rest of the digits to non_negative_num

    non_negative_num = sum_of_digits # Save the Sum

print("Sum is", sum_of_digits)