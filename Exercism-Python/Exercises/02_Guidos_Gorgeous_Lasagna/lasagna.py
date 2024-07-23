EXPECTED_BAKE_TIME = 40

def bake_time_remaining(bake_time_remaining):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return 40 - bake_time_remaining

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes;

    :param number_of_layers: int - number of lasagnas layers.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes number of layers and return the number of preparation time in minuts.
    """
    return 2*number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time;

    :param number_of_layers: int - number of lasagnas layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    
    :return: int - elapsed time (in minutes).

    Function that takes number of layers and elapsed_bake_time return the number of elapsed time in minutes.
    """
    return elapsed_bake_time + 2*number_of_layers
