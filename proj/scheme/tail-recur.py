def thunk_factorial(n, so_far=1):
    def thunk():
        if n == 0:
            return so_far
        return thunk_factorial(n - 1, so_far * n)
    return thunk

def factorial(n):
    
    value = thunk_factorial(n)
    #until here,value is func that haven't called
    while callable(value): # While value is still a thunk
        value = value()
    return value