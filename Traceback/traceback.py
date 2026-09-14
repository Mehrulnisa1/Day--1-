# Python Traceback

import traceback


# 1. What is Traceback?
# Traceback shows where an error happened,
# what caused it, and the sequence of function calls
# that led to the error.


# 2. Automatic Traceback
# Python automatically shows a traceback when
# an unhandled exception occurs.

def divide(a, b):
    return a / b

# divide(10, 0)
# Python automatically displays the traceback.


# 3. Manual Traceback
# We can manually print the traceback
# when we catch an exception.

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Something went wrong.")
    traceback.print_exc()


# 4. Traceback + Logging

import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("Division failed")


# 5. Traceback as a String

try:
    result = 10 / 0

except ZeroDivisionError:
    error_details = traceback.format_exc()
    print(error_details)


# 6. Traceback + Re-raise

def calculate():
    try:
        return 10 / 0

    except ZeroDivisionError:
        logging.exception("Error inside calculate()")
        raise


try:
    calculate()

except ZeroDivisionError:
    print("Error reached the higher level.")