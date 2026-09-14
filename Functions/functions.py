# Basic function

def greet():
    print("Hello, welcome to Python!")


# Calling the function
greet()


# Function with a parameter

def greet_person(name):
    print(f"Hello, {name}")


greet_person("Mehr")


# Function name
def say_hello():
    print("Hello")


say_hello()


# pass
# Used when we want to create a function
# but do not want to implement it yet.

def future_function():
    pass

# return sends a value back from a function

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# Function without return

def show_message():
    print("Hello")


value = show_message()

print("Returned value:", value)





def student(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# Positional arguments
student("Mehr", 22, "Srinagar")


# Keyword arguments
student(name="Mehr", age=22, city="Srinagar")


# Keyword arguments can be in a different order
student(city="Srinagar", age=22, name="Mehr")


# Mixing positional and keyword arguments
student("Mehr", age=22, city="Srinagar")


# Invalid:
# student(name="Mehr", 22, city="Srinagar")
#
# Positional arguments must come before keyword arguments.




# Default parameter

def greet(name="Guest"):
    print(f"Hello, {name}")


# Uses default value
greet()


# Uses the value provided
greet("Mehr")


# Another example

def calculate_total(price, tax=0.05):
    return price + (price * tax)


print(calculate_total(100))

print(calculate_total(100, 0.10))



# *args
# Allows any number of positional arguments

def numbers(*args):
    print("Arguments:", args)
    print("Type:", type(args))


numbers(10, 20, 30, 40)


# Example using *args

def add_numbers(*args):
    return sum(args)


print(add_numbers(10, 20, 30))


# **kwargs
# Allows any number of keyword arguments

def details(**kwargs):
    print("Details:", kwargs)
    print("Type:", type(kwargs))


details(
    name="Mehr",
    age=22,
    city="Srinagar"
)


# Using both *args and **kwargs

def profile(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


profile(
    "Python",
    "AI",
    name="Mehr",
    level="Beginner"
)




# A method is a function associated with an object.

text = "hello python"

# upper() is a string method
print(text.upper())

# replace() is a string method
print(text.replace("python", "world"))


# append() is a list method

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)


# Our own method inside a class

class Student:

    def greet(self):
        print("Hello from Student")


student = Student()

student.greet()



# Python uses object references when passing values to functions.
# This is also called call by sharing.


# Mutable object example
# Lists can be changed inside a function.

def add_subject(subjects):
    subjects.append("Python")


my_subjects = ["HTML", "CSS"]

add_subject(my_subjects)

print(my_subjects)


# Immutable object example
# Reassigning an integer inside the function
# does not change the original variable.

def change_number(number):
    number = 100

    print("Inside function:", number)


value = 10

change_number(value)

print("Outside function:", value)



# Combined function practice

def create_profile(name, age=18, *skills, **details):

    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Other details:", details)


create_profile(
    "Mehr",
    22,
    "Python",
    "HTML",
    "CSS",
    city="Srinagar",
    role="AI/ML Intern"
)


# Positional + keyword arguments

def calculate(a, b, operation="add"):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    else:
        return None


print(calculate(10, 5))

print(calculate(10, 5, "subtract"))

print(calculate(
    a=10,
    b=5,
    operation="add"
))




