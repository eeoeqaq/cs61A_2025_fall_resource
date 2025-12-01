def search (s,value):
    cnt=0
    for element in s:
        if element==value:
            cnt+=1
    return cnt
def a(a,b,f):
    return {y:[x for x in b if f(y,x)==1] for y in a}   