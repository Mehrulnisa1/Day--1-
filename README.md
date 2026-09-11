# Python Virtual Environment + NumPy

This repository is basically my practice project for understanding **Python virtual environments (`venv`), pip, requirements.txt, and NumPy**.

I created this while learning Python for AI/ML, so the explanations are kept simple and practical.

---

## 📁 Project Structure

```text
python-venv-guide/
│
├── venv/                 # My virtual environment (not uploaded to GitHub)
│
├── app/
│   └── main.py           # NumPy practice code
│
├── README.md             # What I learned
├── requirements.txt      # Python packages required by the project
└── .gitignore            # Files/folders Git should ignore
```

---

# 1. What is a Virtual Environment?

A virtual environment is like a **separate room for a Python project**.

Imagine I have two projects:

```text
Project A → needs NumPy version 1
Project B → needs NumPy version 2
```

If I install everything globally, the projects could interfere with each other.

A virtual environment keeps the packages for each project separate.

So:

```text
Project A
   ↓
its own Python packages

Project B
   ↓
its own Python packages
```

This is why we use `venv`.

---

# 2. Creating a Virtual Environment

I created my virtual environment using:

```bash
python -m venv venv
```

The first `venv` means:

> Use Python's built-in virtual environment module.

The second `venv` means:

> Create the virtual environment in a folder called `venv`.

So after running this command, a folder named `venv` is created.

---

# 3. Activating the Virtual Environment

Since I am using **Git Bash on Windows**, I activate it using:

```bash
source venv/Scripts/activate
```

After activation, I should see something like:

```text
(venv)
```

at the beginning of my terminal.

That tells me:

> "I'm currently working inside my virtual environment."

---

# 4. Checking Which Python I Am Using

I can check the Python being used with:

```bash
which python
```

If the virtual environment is active, the path should point toward my project's `venv` folder.

For example:

```text
/c/Users/.../python-venv-guide/venv/Scripts/python
```

This is useful because it confirms that my project is using the Python inside my virtual environment.

---

# 5. What is pip?

`pip` is Python's **package installer**.

Python itself does not contain every library I might need.

For example, if I want to use NumPy, I can install it with:

```bash
python -m pip install numpy
```

Think of pip like an **app store for Python packages**.

I ask pip:

```text
"Please install NumPy."
```

And pip downloads and installs it for me.

---

# 6. Installing NumPy

I installed NumPy using:

```bash
python -m pip install numpy
```

NumPy is a very important Python library for:

* numerical calculations
* arrays
* mathematical operations
* data processing
* AI/ML work

---

# 7. My NumPy Example

Inside `app/main.py`, I used:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Numbers:", numbers)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Total:", np.sum(numbers))
```

When I run:

```bash
python app/main.py
```

I get:

```text
Numbers: [10 20 30 40 50]
Mean: 30.0
Maximum: 50
Minimum: 10
Total: 150
```

### What is happening here?

First:

```python
import numpy as np
```

I'm importing NumPy and giving it the shorter name `np`.

Then:

```python
numbers = np.array([10, 20, 30, 40, 50])
```

I'm creating a NumPy array containing five numbers.

Then NumPy gives me useful functions:

```python
np.mean(numbers)
```

Finds the average.

```python
np.max(numbers)
```

Finds the largest number.

```python
np.min(numbers)
```

Finds the smallest number.

```python
np.sum(numbers)
```

Adds all the numbers together.

---

# 8. What is requirements.txt?

`requirements.txt` is basically a **shopping list of Python packages that my project needs**.

For example:

```text
numpy==2.3.2
```

This tells someone:

> "This project needs NumPy, specifically version 2.3.2."

I created it using:

```bash
python -m pip freeze > requirements.txt
```

Here:

```text
python -m pip freeze
```

shows the packages installed in my environment.

And:

```text
>
```

means:

> Take that output and put it into a file.

So:

```bash
python -m pip freeze > requirements.txt
```

means:

> "Take my installed packages and save them into `requirements.txt`."

---

# 9. Why Do We Need requirements.txt?

Imagine I upload my project to GitHub.

Someone else downloads it.

They don't have my virtual environment.

But they can see:

```text
requirements.txt
```

They can create their own virtual environment and install the required packages:

```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
```

The `-r` means:

> Read the requirements from this file.

So the basic idea is:

```text
My computer
     ↓
requirements.txt
     ↓
Someone else's computer
     ↓
Same required packages installed
```

---

# 10. Why Don't I Upload venv to GitHub?

I don't need to upload the actual `venv` folder.

It can be large and contains files specific to my computer.

Instead, I upload:

```text
requirements.txt
```

Someone can simply create a new environment and install the packages from the requirements file.

So:

```text
venv/
     ❌ Don't upload

requirements.txt
     ✅ Upload
```

---

# 11. .gitignore

I created a `.gitignore` file so Git knows which files it should not upload.

My `.gitignore` contains:

```text
venv/
__pycache__/
*.pyc
.env
```

### `venv/`

Don't upload the virtual environment.

### `__pycache__/`

Python creates this folder while running programs. I don't need to upload it.

### `*.pyc`

These are Python-generated compiled files. They aren't needed in my repository.

### `.env`

This can contain private information such as passwords or API keys, so it should not be uploaded.

---

# 12. Useful Commands I Learned

### Create virtual environment

```bash
python -m venv venv
```

### Activate it

```bash
source venv/Scripts/activate
```

### Check Python location

```bash
which python
```

### Check Python version

```bash
python --version
```

### Install a package

```bash
python -m pip install numpy
```

### See installed packages

```bash
python -m pip list
```

### Save installed packages

```bash
python -m pip freeze > requirements.txt
```

### Install packages from requirements.txt

```bash
python -m pip install -r requirements.txt
```

### Leave the virtual environment

```bash
deactivate
```

---

# 13. The Whole Process

The complete workflow I learned is:

```text
Create project
     ↓
Create virtual environment
     ↓
Activate virtual environment
     ↓
Install required packages
     ↓
Write Python code
     ↓
Run the project
     ↓
Create requirements.txt
     ↓
Add venv to .gitignore
     ↓
Push the project to GitHub
```

---

# What I Learned From This Project

By building this small project, I learned:

* What a Python virtual environment is
* Why projects use virtual environments
* How to create a `venv`
* How to activate a `venv` in Git Bash
* What pip does
* How to install Python packages
* What NumPy is
* How to use a NumPy array
* What `requirements.txt` is
* What `pip freeze` does
* Why we don't upload `venv` to GitHub
* How `.gitignore` works
* How another developer can recreate my environment

This is a small project, but it helped me understand an important part of how real Python projects are set up.
