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