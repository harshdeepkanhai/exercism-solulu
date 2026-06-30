def response(hey_bob):
    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"
    if hey_bob.strip()[-1] == "?" and hey_bob.strip().isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip()[-1] == "?":
        return "Sure."
    if hey_bob.strip().isupper():
        return "Whoa, chill out!"
    return "Whatever."
