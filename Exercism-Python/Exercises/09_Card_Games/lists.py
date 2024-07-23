"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    three_rounds = [number, number+1, number+2]
    return three_rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    for i in range(len(rounds)):
        if rounds[i] == number:
            return True

    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    if hand[len(hand)//2] == card_average(hand) or (hand[0] + hand[-1])/ 2 == card_average(hand):
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    odd_counter = 0
    even_counter = 0

    sum_even = 0
    sum_odd = 0
    
    for i in range(len(hand)):
        if hand[i] % 2 == 0:
            sum_even += hand[i]
            even_counter+=1
        else:
            sum_odd += hand[i]
            odd_counter +=1

    if odd_counter == 0 or even_counter == 0:
        return True
        
    average_even = sum_even / even_counter
    average_odd = sum_odd / odd_counter

    if average_even == average_odd:
        return True
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[2] == 11:
        hand[2] = 22

    return hand
