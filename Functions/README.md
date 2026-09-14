# Python Functions

## What I Learned

In this project, I learned how functions work in Python and how they help make code reusable, organized, and easier to maintain.

I practiced creating functions, passing arguments, returning values, using different types of parameters, working with `*args` and `**kwargs`, using methods, and understanding how Python handles objects when passed to functions.

## Motive

The main motive was to understand how to divide a program into smaller pieces instead of writing all the code together.

A function lets me write a piece of code once and reuse it whenever I need it.

## What is a Function?

A function is a reusable block of code that performs a particular task.

```python
def greet():
    print("Hello")

greet()
```

`def` is used to define a function, `greet` is the function name, and `greet()` calls the function.

## Function Name

The function name is the name we use to identify and call a function.

```python
def calculate_sum():
    return 10 + 20
```

Here, `calculate_sum` is the function name.

## Declaration and Initialization

In Python, we normally define a function using `def`. There is no separate function declaration required like in some other languages.

```python
def greet(name):
    print(name)
```

The parameter `name` is defined when creating the function.

When we call it:

```python
greet("Mehr")
```

`"Mehr"` is the argument passed to the function.

## Return

`return` sends a value back from the function.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

If a function does not return anything, Python returns `None`.

## pass

`pass` is used when we want to create a function but do not want to write its implementation yet.

```python
def future_function():
    pass
```

## Number of Arguments

A function can accept one, multiple, or no arguments.

```python
def greet(name):
    print(name)

def add(a, b):
    return a + b
```

## Positional Arguments

With positional arguments, values are matched according to their position.

```python
def student(name, age):
    print(name, age)

student("Mehr", 22)
```

`"Mehr"` goes to `name` and `22` goes to `age`.

## Keyword Arguments

Keyword arguments are passed using the parameter name.

```python
student(name="Mehr", age=22)
```

The order does not matter when using keyword arguments.

```python
student(age=22, name="Mehr")
```

## Mixing Positional and Keyword Arguments

Positional and keyword arguments can be used together.

However, positional arguments must come before keyword arguments.

```python
def student(name, age, city):
    print(name, age, city)

student("Mehr", age=22, city="Srinagar")
```

## Default Parameters

A default parameter already has a value. If no value is provided, the default value is used.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Mehr")
```

The first call uses `"Guest"` and the second call uses `"Mehr"`.

## `*args`

`*args` allows a function to accept any number of positional arguments.

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)
```

The arguments are collected into a tuple.

## `**kwargs`

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def details(**kwargs):
    print(kwargs)

details(name="Mehr", age=22, city="Srinagar")
```

The arguments are collected into a dictionary.

## Method

A method is a function that belongs to an object or class.

For example:

```python
text = "hello"

text.upper()
```

`upper()` is a string method.

Similarly:

```python
numbers = [1, 2, 3]

numbers.append(4)
```

`append()` is a list method
