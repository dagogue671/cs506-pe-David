"""
Problem 1: Reduce to Zero
Given a non-negtive integer num, return the number of steps to reduce it to zero
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1
from it.
"""

step_counter = 0 # Count the number of steps/iterations

non_negative_number = input('Please Enter a Non-Negative Integer: ')
non_negative_number = int(non_negative_number)

# Check if input is positive or negative
if non_negative_number <= 0:
    while non_negative_number <= 0:
        non_negative_number = input('Please Enter a Non-Negative Integer: ')
        non_negative_number = int(non_negative_number)


while non_negative_number != 0:
    prev_num = non_negative_number # place holder for the non_negative_number
    # Divide by 2 if the non_negative_number is even
    if non_negative_number % 2 == 0:
        non_negative_number /= 2
        non_negative_number = int(non_negative_number)
        print(f"{prev_num} is even; divide by 2 and obtain {non_negative_number}")
        step_counter += 1
    # Subtract by 1 if the non_negative_number is odd
    else:
        non_negative_number -= 1
        print(f"{prev_num} is odd; subtract 1 and obtain {non_negative_number}")
        step_counter += 1

print(f"Number of Steps taken is {step_counter}")