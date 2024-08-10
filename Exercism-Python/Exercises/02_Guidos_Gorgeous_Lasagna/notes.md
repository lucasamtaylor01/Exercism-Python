# About `lasagna.py`

## Table of Contents

- [About `lasagna.py`](#about-lasagnapy)
  - [Table of Contents](#table-of-contents)
  - [01. Introduction](#01-introduction)
  - [02. About PEP 257](#02-about-pep-257)
    - [Examples of use](#examples-of-use)
  - [03. Copilot Changes](#03-copilot-changes)
  - [References](#references)

## 01. Introduction

This exercise has simple logic, but I'm interested in learning about the comment style in Python. I want to follow a pattern to write good comments according to a guide.

## 02. About PEP 257

In general, in modules, classes, functions or methods, it is recommended that we use rEST pattern presented with the following format:

- **Summary**: A brief description of what the function does.
- **Parameters**: List of parameters with their types and descriptions.
- **Return**: Description of what the function returns.

### Examples of use

Let's present examples:

**Module:**

```python
"""
This module provides a general description of its purpose.

It may contain various functions, classes, and global variables.
"""

# Functions and classes of the module go here
```

**Class:**

```python
class MyClass:
    """General description of what this class represents.

    Attributes:
        attribute1 (type): Description of attribute 1.
        attribute2 (type): Description of attribute 2.
    """

    def __init__(self, attribute1, attribute2):
        """Initializes the class with the given attributes.

        :param attribute1: type - Description of attribute 1.
        :param attribute2: type - Description of attribute 2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2
```

**Method:**

```python
class MyClass:
    """General description of what this class represents."""

    def __init__(self, attribute1, attribute2):
        """Initializes the class with the given attributes.

        :param attribute1: type - Description of attribute 1.
        :param attribute2: type - Description of attribute 2.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def my_method(self, parameter):
        """Description of what this method does.

        :param parameter: type - Description of the parameter.
        :return: type - Description of the return value.
        """
        pass
```

**Function:**

```python
def my_function(parameter1, parameter2):
    """Description of what this function does.

    :param parameter1: type - Description of parameter 1.
    :param parameter2: type - Description of parameter 2.
    :return: type - Description of the return value.
    """
    pass
```

## 03. Copilot Changes

1. Correct the parameter name in the `bake_time_remaining` function.
2. Improve the docstrings for clarity and consistency.
3. Use the `EXPECTED_BAKE_TIME` constant in the `bake_time_remaining` function.

---

## References

**van Rossum, G., Warsaw, B., & Coghlan, A.** (n.d.). *PEP 8 – Style Guide for Python Code*. Python Software Foundation. Retrieved from [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

**Goodger, D., & van Rossum, G.** (n.d.). *PEP 257 – Docstring Conventions*. Python Software Foundation. Retrieved from [https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/)

*Note:* This content is made available to the public under the public domain, according to the guidelines of the Python Software Foundation.
