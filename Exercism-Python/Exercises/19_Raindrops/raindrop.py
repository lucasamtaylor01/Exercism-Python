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