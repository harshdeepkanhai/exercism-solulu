def two_fer(name=None):
    """
    Returns a named String if name is provided, else 
    returns the default string
    """
    if name:
        return f"One for {name}, one for me."
    return "One for you, one for me."
    