# Python Errors & Exception Handling

# 1. Types of Errors

# SyntaxError -> Wrong Python syntax
# print("Hello"       # SyntaxError

# Runtime/Error -> Happens while the program is running
# print(10 / 0)       # ZeroDivisionError

# Common errors:
# SyntaxError
# NameError
# TypeError
# ValueError
# ZeroDivisionError
# IndexError
# KeyError
# FileNotFoundError


# 2. try / except

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 3. else
# else runs only when NO exception occurs.

try:
    number = int(input("Enter number: "))
    result = 10 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)


# 4. finally
# finally ALWAYS runs.

try:
    number = int(input("Enter number: "))
    result = 10 / number

except (ValueError, ZeroDivisionError):
    print("Something went wrong.")

finally:
    print("This always runs.")


# 5. Golden Rule of Catching Errors
# Catch an error only when you can:
# - handle it
# - recover from it
# - give useful information
# Otherwise, let it propagate.


# 6. When to catch an error

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Age must be a number.")


# 7. Custom Exception

class InvalidAgeError(Exception):
    pass


age = -1

try:
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

except InvalidAgeError as error:
    print("Custom error:", error)


# 8. try + except + raise

def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")

        return a / b

    except ValueError as error:
        print("Error:", error)


print(divide(10, 0))


# 9. Re-raising

def process_number(number):
    try:
        result = 10 / number
        return result

    except ZeroDivisionError:
        print("Logging the error...")
        raise                    # Re-raises the same exception


try:
    process_number(0)

except ZeroDivisionError:
    print("Handled at a higher level.")


# 10. raise vs re-raise

# raise -> creates/raises an exception
# raise ValueError("Invalid value")

# raise inside except -> re-raises the current exception
#
# except Exception:
#     raise
#
# Re-raising allows the error to move to a higher level
# after logging or doing some local work.