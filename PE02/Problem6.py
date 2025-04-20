"""
Problem 6. Working with Files:
1) Write a Python program that takes a text file as input and returns the number of words of a
given text file.
2) Write a while loop that prompts users for their name. When they enter their name, print a
greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make
sure each entry appears on a new line in the file.
3) Make two files, cats.txt and dogs.txt. Store at least three cat names in the first file and three
names of dogs in the second file. Write a program that tries to read these files and print the
contents of the file to the screen. Wrap your code in a try-except block to catch the
FileNotFound error and print a friendly message if a file is missing.
"""

from pathlib import Path

def get_word_count_from_file():
    
    """This function get's the word count from a user input"""
    
    get_file = input("Please enter the file name located in the Problem6_txt folder: ")
    path = Path(f"Problem6_txt/{get_file}")
    contents = path.read_text()
    print(contents)
    print(f"Word count in {get_file} is",len(contents.split()))

def write_in_guest_book():

    """Program to right in a Guest Book located in Problem6_txt folder"""

    while True:
        get_name = input("Please Enter your name or enter q to quit: ")
        get_file = Path("Problem6_txt/guest_book.txt")

        if get_name == 'q':
            break
        else:
            append = get_file.read_text()
            append += f"{get_name}\n"
            get_file.write_text(append)
            print(f"Greetings {get_name}")

def read_two_files():

    """Function to read two text files from the Problem6_txt folder cats.txt and dogs.txt"""

    append = "" 

    try:
        contents1 = Path("Problem6_txt/cats.txt")
        append += contents1.read_text()
    except FileNotFoundError:
        print(f"The file {contents1} is not found.")

    try:
        contents2 = Path("Problem6_txt/dogs.txt")
        append += "\n" + contents2.read_text()
    except FileNotFoundError:
        print(f"The file {contents2} is not found.")
    
    print(append)