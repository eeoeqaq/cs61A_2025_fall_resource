def prefix(s):
    if s:
        yield from prefix(s[:-1])
        yield s

def substr(s):
    if s:
        yield from prefix(s)
        yield from substr(s[1:]) 
