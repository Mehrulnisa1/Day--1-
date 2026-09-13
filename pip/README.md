# Python pip

This folder contains what I learned about **pip**, Python's package manager.

## What is pip?

`pip` is the package installer for Python.

It allows us to:

* Install Python packages
* Remove packages
* Check installed packages
* Check package information
* Manage project dependencies
* Create a `requirements.txt` file

---

# 1. Check pip version

```bash
pip --version
```

This shows the installed pip version and the Python environment that pip belongs to.

---

# 2. Install a package

```bash
pip install numpy
```

This installs the NumPy package.

In this project, NumPy is used in `pip_demo.py`.

---

# 3. Use an installed package

After installing NumPy, we can use it in Python:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Numbers:", numbers)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
```

Output:

```text
Numbers: [10 20 30 40 50]
Mean: 30.0
Maximum: 50
Minimum: 10
```

---

# 4. Check installed packages

```bash
pip list
```

`pip list` displays the packages currently installed in the environment.

Example:

```text
Package    Version
---------  -------
numpy      2.x.x
pip        ...
```

---

# 5. pip freeze

```bash
pip freeze
```

`pip freeze` displays installed packages with their exact versions.

Example:

```text
numpy==2.x.x
```

This format is useful for creating a dependency file.

---

# 6. Create requirements.txt

We can save the output of `pip freeze` into a file:

```bash
pip freeze > requirements.txt
```

Here:

* `pip freeze` gets the installed packages and versions.
* `>` redirects the output into a file.
* `requirements.txt` stores the dependencies.

Example:

```text
numpy==2.x.x
```

---

# 7. Install packages from requirements.txt

If another developer gets this project, they don't need to install every package manually.

They can run:

```bash
pip install -r requirements.txt
```

Pip reads the file and installs the listed dependencies.

---

# 8. Uninstall a package

To remove a package:

```bash
pip uninstall numpy
```

Pip asks for confirmation before uninstalling it.

---

# 9. Show package information

```bash
pip show numpy
```

This displays information about NumPy, such as:

* Package name
* Version
* Installation location
* Dependencies

---

# 10. Check dependencies

```bash
pip check
```

This checks whether installed packages have compatible dependencies.

If everything is correct, pip may display:

```text
No broken requirements found.
```

---

# pip list vs pip freeze

## pip list

```bash
pip list
```

Used mainly to **view installed packages** in a readable format.

## pip freeze

```bash
pip freeze
```

Used to output packages and versions in a format that can be saved to `requirements.txt`.

---

# Important Commands

| Command                           | Purpose                            |
| --------------------------------- | ---------------------------------- |
| `pip --version`                   | Check pip version                  |
| `pip install numpy`               | Install NumPy                      |
| `pip list`                        | List installed packages            |
| `pip freeze`                      | Show packages with versions        |
| `pip freeze > requirements.txt`   | Create/update requirements.txt     |
| `pip install -r requirements.txt` | Install dependencies from the file |
| `pip uninstall numpy`             | Remove NumPy                       |
| `pip show numpy`                  | Show package information           |
| `pip check`                       | Check dependency compatibility     |

---

# Project Structure

```text
pip/
├── pip_demo.py
├── README.md
└── requirements.txt
```

---

# What I Learned

Through this project, I learned:

1. What pip is
2. How to check the pip version
3. How to install Python packages
4. How to use an installed package
5. How to view installed packages using `pip list`
6. What `pip freeze` does
7. How to create `requirements.txt`
8. How to install dependencies from `requirements.txt`
9. How to uninstall packages
10. How to view package information using `pip show`
11. How to check dependencies using `pip check`
12. The difference between `pip list` and `pip freeze`
13. Why `requirements.txt` is useful in a project
