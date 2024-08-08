def leap_year(year):
    """
    Determines if a given year is a leap year.

    :param year: The year to be checked.
    :type year: int
    :return: True if the year is a leap year, False otherwise.
    :rtype: bool
    """
    
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
