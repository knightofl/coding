def f1(s):
    return s.upper()

def f2(s):
    return s[-1::-1]

def f3(s):
    return s+'!'

print(f3(f2(f1('data'))))

def f4(s, *f):
    for fun in f:
        s = fun(s)
    return s

print(f4('data', f1))
print(f4('data', f1, f2))
print(f4('data', f1, f2, f3))


print((lambda x: f1(x))('data'))

