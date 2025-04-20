"""
Problem 5. Object Oriented Programming:
1) Make a class called User. Create two attributes called first_name and last_name, and then
create several other attributes that are typically stored in a user profile. Make a method called
describe_user() that prints a summary of the user's information. Make another method called
greet_user() that prints a personalized greeting to the user. Create 2 instances representing
different users, and call both methods for each user.
2) Write a program to show how multilevel inheritance works
"""

class Users:

    """A Users class"""

    def __init__(self, first_name, last_name, description):
        """Initialize Attributes for All Users"""
        self.first_name = first_name
        self.last_name = last_name
        self.description = description

    def describe_user(self):
        """print function that prints the description of the user"""
        print(f"{self.first_name} {self.last_name} is",self.description)

    def greet_user(self):
        """print function to greet the user"""
        print(f"Hello {self.first_name} {self.last_name}")



class SuperUser(Users):

    """Super User Class that is inherited from the User Class"""

    def __init__(self, first_name,last_name, description, is_superuser=True):
        """Initialize attributes for Super Users"""
        super().__init__(first_name,last_name,description)
        self.is_superuser = is_superuser


    
    def access_type(self):
        """Check for Super User Access"""
        if self.is_superuser:
            print(f"{self.first_name} {self.last_name} has Super User Access")
        else:
            print(f"{self.first_name} {self.last_name} does not have Super User Access")


class StandardUser(SuperUser):

    """Child class of the Super User Class"""

    def __init__(self, first_name, last_name, description, is_superuser=False):
        """Initialize Attributes for a Standard User"""
        super().__init__(first_name, last_name, description, is_superuser)



# Test Users Class and Attributes
user_david = Users("David", "Gogue", "Just a guy")
user_david.greet_user()
user_david.describe_user()

# Test to check if User has an Access Type

try:
    user_david.access_type()
except AttributeError:
    print(f"{user_david.first_name} {user_david.last_name} does not have an Access Type")

print("\n")

# Checks Super User class and Attributes
user_yuki = SuperUser("Yuki","Shimizu","Just a Girl")
user_yuki.greet_user()
user_yuki.describe_user()
user_yuki.access_type()
print("\n")

# Checks Standard User class and attributes
user_chuck = StandardUser("Chuck","Lidell","Just a Standard User")
user_chuck.greet_user()
user_chuck.describe_user()
user_chuck.access_type()
print("\n")
    





