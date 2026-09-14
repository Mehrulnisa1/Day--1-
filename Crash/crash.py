# Python Crash / Unhandled Exceptions

# 1. What is a Crash?
# A program "crashes" when an unhandled error/exception
# stops normal program execution.

# Example:
# number = 10 / 0
# ZeroDivisionError -> program stops


# 2. Types of Crash / Failure

# A) Unhandled Exception
# An exception occurs and nobody catches it.

# 10 / 0


# B) Crash caused by invalid input/state
# Example:
# int("hello") -> ValueError


# C) Crash caused by programmer bugs
# Example:
# print(name) -> NameError if name doesn't exist


# D) System/resource failures
# Examples:
# File not found
# Database unavailable
# Network failure
# Out of memory


# 3. When to Let It Crash

# Let the program fail when it cannot safely or meaningfully
# continue.

# Example: unexpected programming bug

def calculate():
    return 10 / 0

# Don't hide the bug with:
#
# try:
#     calculate()
# except Exception:
#     pass
#
# Letting it fail makes the problem visible.


# 4. Golden Rule

# Catch an error ONLY when you can meaningfully handle it.
#
# If you can recover -> catch it.
# If you cannot recover -> let it propagate/crash.


# 5. When NOT to Let It Crash

# Catch expected/recoverable problems.

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid number.")


# The user made an input mistake,
# so we can recover and continue.


# 6. Why is crashing useful?

# A controlled failure can:
# - expose programming bugs
# - prevent incorrect results
# - prevent corrupted data
# - make serious problems visible
# - help developers debug the application


# 7. Where is crashing / failure handling used?

# Development:
# Find and fix programming bugs.

# APIs / Backend:
# Unexpected server errors should not be silently ignored.

# Databases:
# If an important database operation fails,
# continuing may cause incorrect data.

# Security:
# Dangerous or invalid states should not be ignored.

# Production:
# Log the error, clean up resources,
# and fail safely when necessary.


# 8. Catch vs Crash

def process_data(data):

    if not isinstance(data, int):
        raise TypeError("Data must be an integer")

    return data * 2


# Recoverable error -> catch it
try:
    value = int("hello")

except ValueError:
    print("Invalid user input.")


# Unexpected/programming error -> don't hide it
result = process_data("hello")
# TypeError propagates and the program stops.