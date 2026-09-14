# Python Logging

This project covers Python logging and how it is used for debugging, monitoring, and recording program events.

## Topics Covered

* **Why Logging** – Records program events, warnings, and errors for debugging and monitoring.
* **Print vs Logging** – `print()` displays information; logging records information with levels, timestamps, and destinations.
* **Logging Levels** – `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
* **`basicConfig()`** – Configures the basic logging system.
* **Timestamps** – Added using `%(asctime)s`.
* **`logging.error()`** – Records an error message.
* **`logging.exception()`** – Records the error message plus traceback; normally used inside `except`.
* **Logging + try/except** – Logs errors when exceptions are caught.
* **Loggers** – Created using `logging.getLogger()` to manage application logs.
* **Handlers** – Decide where logs are sent, such as the console or a file.
* **FileHandler** – Saves logs to a file such as `app.log`.
* **StreamHandler** – Sends logs to the console.

## Basic Structure

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

### Error vs Exception

```text
logging.error()      → error message
logging.exception()  → error + traceback
```

### Logger Flow

```text
Logger → Handler → Destination
                    ↓
              Console / File
```

No external packages are required.
