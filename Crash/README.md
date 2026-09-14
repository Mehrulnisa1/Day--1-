# Python Crash / Failure Handling

This project covers what a program crash is, when to let an error crash the program, when to catch it, and why controlled failure is useful.

## Topics Covered

* **Crash** – When an unhandled exception stops normal program execution.
* **Types of Failure** – Unhandled exceptions, invalid input/state, programming bugs, and system/resource failures.
* **When to Let It Crash** – When the error is unexpected and the program cannot safely or meaningfully continue.
* **When NOT to Let It Crash** – When the error is expected and can be handled or recovered from.
* **Golden Rule** – Catch an error only when you can meaningfully handle it; otherwise, let it propagate.
* **Why Crash?** – To expose bugs, prevent incorrect results, protect data, and make serious failures visible.
* **Where Used** – Backend applications, APIs, databases, security-sensitive code, and production systems.

### Simple Rule

```text id="f70xw4"
Recoverable error → Catch and handle it
Unexpected error   → Let it propagate/crash
```

### Important

Crashing does **not** mean intentionally breaking the program.

It means allowing an **unhandled serious exception** to stop normal execution instead of silently hiding the problem.

No external packages are required.
