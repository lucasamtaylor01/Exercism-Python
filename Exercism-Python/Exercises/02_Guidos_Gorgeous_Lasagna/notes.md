# About `lasagna.py`

## Introduction

This exercise has simple logic, but I'm interested in learning about the comment style in Python. I want to follow a pattern to write good comments according to a guide.

## About PEP 257

In general, in modules, classes, functions or methods, it is recommended that we use rEST pattern presented with the following format:

- **Summary**: A brief description of what the function does.
- **Parameters**: List of parameters with their types and descriptions.
- **Return**: Description of what the function returns.

## Examples of use

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

## References

[1] [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

[2] [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
