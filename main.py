def gen(a,b):
    yield a+b
    yield a-b
    yield a*b
x=gen(4,6)
print(next(x))
print(next(x))
print(next(x))
