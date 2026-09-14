# Python Traceback

This project covers **traceback**, including automatic and manual traceback, traceback with logging, and re-raising exceptions.

## Topics Covered

* **Traceback** – Shows where an exception occurred and the sequence of function calls that led to it.
* **Automatic Traceback** – Python automatically displays a traceback when an exception is not handled.
* **Manual Traceback** – `traceback.print_exc()` can display the traceback inside an `except` block.
* **Traceback as String** – `traceback.format_exc()` stores the traceback as a string.
* **Traceback + Logging** – `logging.exception()` automatically includes traceback information.
* **Traceback + Re-raise** – Log the traceback and use `raise` to send the original exception to a higher level.

### Automatic vs Manual

```text
Automatic → Python shows traceback automatically
Manual    → Developer catches the error and prints/logs traceback
```

### Useful Functions

```python
traceback.print_exc()
traceback.format_exc()
```

### With Logging

```python
except Exception:
    logging.exception("Something went wrong")
```

No external packages are required.
