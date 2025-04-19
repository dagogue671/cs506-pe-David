"""
Problem 4. Adding numbers
One common problem when prompting for numerical input occurs when people provide text instead of
numbers. When you try to convert the input to an int, you'll get a ValueError. Write a program that
prompts for two numbers. Add them together and print the result. Catch the ValueError if either input
value is not a number and print a friendly error message. Test your program by entering two numbers
and then by entering some text instead of a number.
"""


print("Give me two numbers, and I'll add them")
print("Else Enter 'q' to quit.")

while True:

    first_number = input("Please input first number ")
    if first_number == 'q':
        break
    
    try:
        first_number = int(first_number)
    except ValueError:
        print("First number is not a number\n")
        continue
    else:
        
        second_number = input("Please enter second number: ")
        
        if second_number == 'q':
            break
        try:
            second_number = int(second_number)
        except ValueError:
            print("Second Number is not a number\n")
            
        else:
            print("Total is: ", first_number + second_number, "")
            break
    

        

