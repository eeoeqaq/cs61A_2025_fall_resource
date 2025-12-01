def improve(update,close,value=1):
    while not close(value):
        value=update(value)
    return value

def approx(x,y,diff=1e-5):
    return abs(x-y)<diff


def main(f,df):
    def local_approx(x):
        return approx(f(x),0)
    def newton_update(x):
        x=x-f(x)/df(x)
        return x
    return improve(newton_update,local_approx)

def local_sqrt(a):
    #def f(x):
     #   return x * x - a
    #def df(x):
     #   return 2 * x
    return main(lambda x:x*x-a, lambda x:2*x)

def trace(fn):
    def wrapped(x):
        print(fn(x))
        return fn(x)
    return wrapped

@ trace
def triple(x):
    return x*x*x

const=10 
def1023=lambda x:x*x
def1024=lambda x:x*x*x
def1025=local_sqrt
a=def1023
a=def1024
a=def1025







