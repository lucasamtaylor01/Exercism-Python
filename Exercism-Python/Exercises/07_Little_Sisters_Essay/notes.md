
# Comments and Observations About the Exercise

## 01. Introduction

According to Exercism, the main objective of this exercise is: "This learning exercise helped evolve your knowledge of String Methods."

I always forget the functions when I'm working with *strings*, so in these notes, I am going to write a little description about the functions that I used to solve it.

## 02. Functions Used and Examples

### Example of `title()`

**Input:**

```python
    str = "example for notes"
    print(str.title())
```

**Output:**

```plaintext
    Example for Notes
```

### Example of `strip()`

**Input:**

```python
    str = "      example for notes.              " 
    print(str.strip())
```

**Output:**

```plaintext
    example for notes. 
```

**Observation:** The `strip()` function in Python removes whitespace from the beginning and end of a string, but does not remove whitespace in the middle of the string.

---

## References

1. `title()` - Python Reference. © Copyright 2015, Jakub Przywóski. Available at: <https://python-reference.readthedocs.io/en/latest/docs/str/title.html> (Accessed: 10 August 2024).

2. `strip()` - Python Reference. © Copyright 2015, Jakub Przywóski. Available at: <https://python-reference.readthedocs.io/en/latest/docs/str/strip.html> (Accessed: 10 August 2024).
