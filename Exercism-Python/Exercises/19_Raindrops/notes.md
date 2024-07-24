# Notes about the exercise

## My attempt
``` python
def convert(number):
    if number % 3 == 0:
        if number % 5 == 0:
            if number % 7 == 0:
                return "PlingPlangPlong"
            else:
                return "PlingPlang"
        else:
            if number % 7 == 0:
                return "PlingPlong"
            else:
                return "Pling"
    elif number % 5 == 0:
        if number % 7 == 0:
                return "PlangPlong"
        else:
            return "Plang"

    elif number % 7 == 0:
        return "Plong"

    else:
        return str(number)
```

## CHATGPT's correction

```python
def convert(number):
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result if result else str(number)
``` 

*Observation:* Watch later [14 Ways to Solve Raindrops (FizzBuzz, but harder!)](https://www.youtube.com/watch?v=mwe-9RIV39Y)