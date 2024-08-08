def equilateral(sides):
    """
    Determines if a triangle is equilateral.

    :param sides: A list of three integers or floats representing the lengths of the sides of a triangle.
    :return: True if the triangle is equilateral, False otherwise.
    """
    if Triangle_Inequality(sides) == False:
        return False

    if Is_there_zero(sides) == False:
        return False
        
    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False


def isosceles(sides):
    """
    Determines if a triangle is isosceles.

    :param sides: A list of three integers or floats representing the lengths of the sides of a triangle.
    :return: True if the triangle is isosceles, False otherwise.
    """
    if Triangle_Inequality(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    """
    Determines if a triangle is scalene.

    :param sides: A list of three integers or floats representing the lengths of the sides of a triangle.
    :return: True if the triangle is scalene, False otherwise.
    """
    if Triangle_Inequality(sides) == False:
        return False
        
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True
    else:
        return False


def Triangle_Inequality(sides):
    """
    Checks if the sides of a triangle satisfy the triangle inequality theorem.

    :param sides: A list of three integers or floats representing the lengths of the sides of a triangle.
    :return: True if the sides satisfy the triangle inequality, False otherwise.
    """
    if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    else:
        return False


def Is_there_zero(sides):
    """
    Checks if any side of the triangle is zero.

    :param sides: A list of three integers or floats representing the lengths of the sides of a triangle.
    :return: False if any side is zero, otherwise None.
    """
    for i in range(3):
        if sides[i] == 0:
            return False
