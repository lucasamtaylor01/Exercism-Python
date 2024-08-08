def response(hey_bob):
    """
    Generate a response to Bob's conversational partner based on the input.

    Bob's conversational rules are as follows:
    - If the input is empty or only whitespace, respond with "Fine. Be that way!".
    - If the input is in all uppercase letters and ends with a question mark, respond with "Calm down, I know what I'm doing!".
    - If the input is in all uppercase letters, respond with "Whoa, chill out!".
    - If the input ends with a question mark, respond with "Sure.".
    - For any other input, respond with "Whatever.".

    :param hey_bob: A string input representing a statement or question directed at Bob.
    :return: A string response from Bob based on the input.
    """
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
