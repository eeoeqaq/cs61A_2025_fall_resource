def make_adder(n):
    def adder(k):
        return n+k
    return adder

a=make_adder(3)
b=a(4)
print(b)
make_adder(1)(2)