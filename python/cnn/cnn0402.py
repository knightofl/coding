d1 = {'a':1, 'b':2, 'c':3, 'd':4}
print(d1['c'])
print(d1.get('b'))
print(d1.get('e'))

d11 = d1.setdefault('e', 5)
print(d11)
print(d1)

d12 = d1.get('f', 6)
print(d12)
print(d1)

print(d1.pop('e'))
print(d1)

print(d1.popitem())
print(d1)

d1.clear()
print(d1)

d2 = {}
print(d2, type(d2))

s1 = set(d2)
print(s1, type(s1))
s2 = set()
print(s2, type(s2))

d3 = {1}
print(d3, type(d3))

d4 = dict(a=10, b=20)
print(d4)

d4['c'] = 40
print(d4)
print(len(d4))


k1 = ['k1', 'k2', 'k3']
v1 = [10, 20, 30]
d5 = dict(zip(k1, v1))

print(d5)
print(d5.keys(), d5.values())
print('k1' in d5.keys())
print(30 in d5.values())
print(d5.items())
print(('k1',10) in d5.items())

for k in d5:
    print(k, end=' ')
print()

for k in d5:
    print(d5[k], end=' ')
print()

for k in d5.keys():
    print(k, end=' ')
print()

for v in d5.values():
    print(v, end=' ')
print()

for k,v in d5.items():
    print(v, k)

d6 = zip(k1, v1)
print(type(d6))
print(next(d6))
print(next(d6))

en = enumerate(d5)
print(type(en))
print(next(en))
print(next(en))

it = iter(d5)
print(type(it))
print(next(it))
print(next(it))