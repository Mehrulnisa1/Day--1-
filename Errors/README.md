# Python Errors & Exception Handling

This project covers Python errors and exception handling, including **types of errors, `try`, `except`, `else`, `finally`, the golden rule of catching errors, custom exceptions, `raise`, and re-raising**.

### Types of Errors

* `SyntaxError` → incorrect Python syntax
* `NameError` → variable/name doesn't exist
* `TypeError` → wrong data type
* `ValueError` → correct type but invalid value
* `ZeroDivisionError` → division by zero
* `IndexError` → invalid list index
* `KeyError` → missing dictionary key
* `FileNotFoundError` → file doesn't exist

### Exception Handling

```text
try       → code that may fail
except    → handles the error
else      → runs when no error occurs
finally   → always runs
```

### Golden Rule

**Catch an error only when you can meaningfully handle, recover from, or explain it. Otherwise, let it propagate.**

### Custom Exceptions

Create your own exception using a class that inherits from `Exception`.

### `raise`

Used to intentionally create an exception.

```python
raise ValueError("Invalid value")
```

### Re-raising

Using `raise` inside an `except` block sends the **same exception upward** after doing something locally, such as logging it.

```python
except Exception:
    log_error()
    raise
```

**`raise` → raise an exception**
**`raise` inside `except` → re-raise the current exception**
