# Python Logging

import logging


# 1. Why Logging?
# Logging records what is happening inside a program.
# It is useful for debugging, monitoring, and finding problems.
#
# print() -> mainly for displaying information to the user
# logging -> for recording program events and errors


# 2. Logging Levels
#
# DEBUG    -> detailed information for debugging
# INFO     -> normal program information
# WARNING  -> something may be wrong
# ERROR    -> an error occurred
# CRITICAL -> serious error


# 3. basicConfig()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debug message")       # Not shown because level is INFO
logging.info("Program started")
logging.warning("This is a warning")
logging.error("Something went wrong")
logging.critical("Critical problem")


# 4. Logging + try/except

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    logging.info("Calculation successful")
    print(result)

except ValueError:
    logging.error("User entered an invalid number")

except ZeroDivisionError:
    logging.error("User tried to divide by zero")


# 5. logging.error() vs logging.exception()

try:
    number = 10 / 0

except ZeroDivisionError:
    logging.error("Division failed")


try:
    number = 10 / 0

except ZeroDivisionError:
    logging.exception("Division failed")


# error() -> logs the error message
# exception() -> logs the error + traceback
#
# logging.exception() should normally be used INSIDE an except block.


# 6. Logger

logger = logging.getLogger(__name__)

logger.info("Message from my logger")
logger.warning("Warning from my logger")
logger.error("Error from my logger")


# 7. Handler
# A handler decides WHERE logs go.
#
# StreamHandler -> console
# FileHandler   -> file

file_handler = logging.FileHandler("app.log")

file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.error("This error is saved in app.log")


# 8. Logger + Handler + File

app_logger = logging.getLogger("my_app")
app_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.ERROR)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

app_logger.addHandler(console_handler)
app_logger.addHandler(file_handler)

app_logger.info("Application started")
app_logger.warning("Something may need attention")
app_logger.error("Application error")