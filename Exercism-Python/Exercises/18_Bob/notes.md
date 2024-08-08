## Notes about the exercise

# First try

```python
def response(hey_bob):
    for i in range(len(hey_bob)):
        if hey_bob[i] != "\n" or hey_bob[i] != "\t" or hey_bob[i] != " " or hey_bob[i] != "":
            if  hey_bob[-1] == "?" and hey_bob.isupper():
                return "Calm down, I know what I'm doing!"
            elif hey_bob[-1] == "?":
                return "Sure."
            elif hey_bob.isupper():
                return "Whoa, chill out!"
            else:
                return "Whatever."
        else:
            return "Fine. Be that way!"
    
```

**Comments**

1. 20/25 tests passed;
2. `hey_bob[i] != "\n" or hey_bob[i] != "\t" or hey_bob[i] != " " or hey_bob[i] != ""` too much information here

## CHATGPT's help

```python
def response(hey_bob):

    hey_bob = hey_bob.strip()
    
    if hey_bob == "":
        return "Fine. Be that way!"
    
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    
    if hey_bob.endswith("?"):
        return "Sure."
    
    return "Whatever."
```

**Comments**

1. 24/25 tests passed;
2. More clear

Let's organize the functions that I didn't know before:

1. `strip()`: String specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.

    *Reference:* <https://python-reference.readthedocs.io/en/latest/docs/str/strip.html>

2. `endswith("?")`: Returns a Boolean stating whether a string ends with the specified suffix.

    *Reference:* <https://python-reference.readthedocs.io/en/latest/docs/str/endswith.html>
