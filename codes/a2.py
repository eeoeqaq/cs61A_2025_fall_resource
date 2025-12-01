from operator import floordiv, mod
def pfctdiv(a,b=10):
    """better division!
    >>> a,b=pfctdiv(2493,10)
    >>> a
    249
    >>> bq
    3
    """
    return floordiv(a,b),mod(a,b)


#

