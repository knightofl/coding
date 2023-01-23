import re


def clr_str(str_data):
    result = []

    for s in str_data:
        s = s.strip()
        s = re.sub('[!#?]', '', s)
        s = s.title()

        result.append(s)
    
    return s


def f1(s):
    return s.strip()

def f2(s):
    return re.sub('[!#?]', '', s)

def f3(s):
    return s.title()


def f4(s, *f):
    r = []
    for st in s:
        for fun in f:
            st = fun(st)
        r.append(st)
    return r

s = ['newyork ', 'l.a.', 'chicago!', '##san fransisco##', ' busan?']

print(f4(s, f1))
print(f4(s, f1, f2))
print(f4(s, f1, f2, f3))
