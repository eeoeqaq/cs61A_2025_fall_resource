def minimum_mewtations(typed: str, source: str, limit: int) -> int:
    """A diff function for autocorrect that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if typed==source:
        return 0
    if limit<0:
        return 666

    else:
        add = 1+minimum_mewtations(source[0]+typed, source, limit-1)
        remove = 1+minimum_mewtations(typed[1:], source, limit-1)
        substitute = (typed[0]!=source[0])+minimum_mewtations(typed[1:], source[1:], limit-(typed[0]!=source[0]))
        return min(add,remove,substitute)
    

def furry_fixes(typed: str, source: str, limit: int) -> int:
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths to this value and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if limit<0:
        return 1
    if(len(typed)==0 or len(source)==0):
        return abs(len(typed)-len(source))
    return int(typed[0]!=source[0])+furry_fixes(typed[1:],source[1:],limit-int(typed[0]!=source[0]))
    # END PROBLEM 6
