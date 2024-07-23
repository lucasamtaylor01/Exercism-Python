def equilateral(sides):
    if Triangle_Inequality(sides) == False:
        return False

    if Is_there_zero(sides) == False:
        return False
        
    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False



def isosceles(sides):
    if Triangle_Inequality(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        else:
            return False
    else:
        return False
    



def scalene(sides):
    if Triangle_Inequality(sides) == False:
        return False
        
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True
    else:
        return False


def Triangle_Inequality(sides):
    if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    else:
        return False


def Is_there_zero(sides):
    for i in range(3):
        if sides[i] == 0:
            return False
