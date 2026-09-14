# Integers

age = 21
marks = 85
year = 2026

print("Age:", age)
print("Marks:", marks)
print("Year:", year)

# Arithmetic operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Check data type
print(type(age))




# Strings

name = "Mehr"
message = "Hello Python"

print(name)
print(message)

# String length
print("Length:", len(name))

# Accessing characters
print("First character:", name[0])
print("Last character:", name[-1])

# Slicing
text = "Python Programming"

# Slice from start
print(text[:6])

# Slice to end
print(text[7:])

# Slice with start and end
print(text[0:6])

# Negative indexing
print(text[-1])
print(text[-3:])

# Modify string
# Strings are immutable, so we cannot directly change a character.

# This would cause an error:
# name[0] = "M"

# Instead, create a new string
name = "M" + name[1:]
print(name)

# Remove white spaces
text = "   Hello Python   "
print(text.strip())

# Replace
text = "I like Java"
print(text.replace("Java", "Python"))

# Concatenation
first_name = "Mehr"
last_name = "R"

full_name = first_name + " " + last_name
print(full_name)

# f-string
age = 21
print(f"My name is {name} and I am {age} years old.")

# Escape characters
print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Hello\"")
print("It's Python")
print("C:\\Users\\Hp")




# String Methods

text = "  Hello Python World  "

# Change case
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# Remove spaces
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Replace
print(text.replace("Python", "Java"))

# Split
words = text.split()
print(words)

# Join
names = ["Mehr", "Ali", "Sara"]
print(" - ".join(names))

# Find
print(text.find("Python"))

# Count
print(text.count("o"))

# Starts with
print(text.strip().startswith("Hello"))

# Ends with
print(text.strip().endswith("World"))

# Check alphabet
word = "Python"
print(word.isalpha())

# Check number
number = "12345"
print(number.isdigit())

# Check alphanumeric
value = "Python123"
print(value.isalnum())

# Check lowercase
print("hello".islower())

# Check uppercase
print("HELLO".isupper())

# Check whitespace
print("   ".isspace())

# Length
print(len(text))




# Boolean

is_student = True
is_working = False

print(is_student)
print(is_working)

print(type(is_student))

# Comparisons

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators

age = 21

print(age > 18 and age < 30)
print(age < 18 or age > 20)
print(not age < 18)

# Boolean from values

print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))
print(bool([]))
print(bool([1, 2, 3]))



# List Methods

numbers = [5, 2, 8, 1, 3, 2]

print(numbers)

# append()
numbers.append(10)
print("append:", numbers)

# insert()
numbers.insert(1, 20)
print("insert:", numbers)

# extend()
numbers.extend([30, 40])
print("extend:", numbers)

# remove()
numbers.remove(2)
print("remove:", numbers)

# pop()
removed_item = numbers.pop()
print("Removed:", removed_item)
print("pop:", numbers)

# index()
print("Index of 8:", numbers.index(8))

# count()
print("Count of 2:", numbers.count(2))

# sort()
numbers.sort()
print("sort:", numbers)

# reverse()
numbers.reverse()
print("reverse:", numbers)

# copy()
new_numbers = numbers.copy()
print("Copied list:", new_numbers)

# clear()
new_numbers.clear()
print("Cleared list:", new_numbers)



# Tuples

numbers = (10, 20, 30, 40)

print(numbers)

# Accessing
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:3])

# Length
print(len(numbers))

# Count
print(numbers.count(20))

# Index
print(numbers.index(30))

# Tuple with one item
single_item = (10,)
print(single_item)

# Tuple unpacking

person = ("Mehr", 21, "MCA")

name, age, course = person

print(name)
print(age)
print(course)

# Tuples are immutable

# This will cause an error:
# numbers[0] = 100




# Sets

numbers = {1, 2, 3, 4, 5}

print(numbers)

# Sets do not allow duplicates

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# Add
numbers.add(10)
print(numbers)

# Add multiple values
numbers.update([20, 30, 40])
print(numbers)

# Remove
numbers.remove(10)
print(numbers)

# Discard
numbers.discard(100)
print(numbers)

# Pop
removed = numbers.pop()
print("Removed:", removed)
print(numbers)

# Length
print(len(numbers))

# Membership
print(20 in numbers)


# Dictionaries

person = {
    "name": "Mehr",
    "age": 21,
    "course": "MCA"
}

print(person)

# Accessing values

print(person["name"])
print(person["age"])

# Using get()

print(person.get("course"))

# Change value

person["age"] = 22
print(person)

# Add new key-value pair

person["city"] = "Srinagar"
print(person)

# Remove using pop()

person.pop("city")
print(person)

# Remove last item

person["city"] = "Srinagar"
person.popitem()
print(person)

# Delete

person["city"] = "Srinagar"
del person["city"]
print(person)

# Check key

print("name" in person)

# Length

print(len(person))

# Keys

print(person.keys())

# Values

print(person.values())

# Items

print(person.items())

# Copy

person_copy = person.copy()
print(person_copy)

# Clear

person_copy.clear()
print(person_copy)



# Dictionary Methods

student = {
    "name": "Mehr",
    "age": 21,
    "course": "MCA"
}

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# get()
print(student.get("name"))

# update()
student.update({"age": 22})
print(student)

# setdefault()

student.setdefault("city", "Srinagar")
print(student)

# pop()

student.pop("city")
print(student)

# popitem()

student["city"] = "Srinagar"
student.popitem()
print(student)

# copy()

student_copy = student.copy()
print(student_copy)

# clear()

student_copy.clear()
print(student_copy)

# fromkeys()

keys = ["name", "age", "course"]
new_student = dict.fromkeys(keys)

print(new_student)

# fromkeys with default value

new_student = dict.fromkeys(keys, "Not Available")
print(new_student)





# Mutable and Immutable Data Types

# Immutable example - String

name = "Mehr"

# We cannot directly modify a character
# name[0] = "A"

# Instead, a new string is created

name = "A" + name[1:]

print(name)


# Immutable example - Tuple

numbers = (1, 2, 3)

# numbers[0] = 100
# This gives an error because tuples are immutable.


# Mutable example - List

fruits = ["apple", "banana"]

fruits[0] = "orange"

print(fruits)


# Mutable example - Dictionary

student = {
    "name": "Mehr",
    "age": 21
}

student["age"] = 22

print(student)


# Mutable example - Set

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)



# List Comprehension

# Normal way

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)


# List comprehension

numbers = [i for i in range(1, 6)]

print(numbers)


# Squares

squares = [i * i for i in range(1, 6)]

print(squares)


# Even numbers

even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)


# Odd numbers

odd_numbers = [i for i in range(1, 11) if i % 2 != 0]

print(odd_numbers)


# Convert strings to uppercase

names = ["mehr", "ali", "sara"]

upper_names = [name.upper() for name in names]

print(upper_names)


# Conditional expression

numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)




