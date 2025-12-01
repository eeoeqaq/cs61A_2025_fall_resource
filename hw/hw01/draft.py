def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
#这个 improve 函数是
# 迭代求精（repetitive refinement）的通用表达式。
# 它并不会指定要解决的问题，而是会将这些细节留给作为参数传入的 update 和 close 函数。
def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

def average(x, y):
    return (x + y)/2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)