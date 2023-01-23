a = ('a1','a2','a3','a4')
b = ('b1','b2','b3','b4')

q, w, e, r = a
print(q, w, e, r)

j, *k, l = b
print(j, k, l)

c = a + b
print(c)

print(c[3])
print(c[6:])
print(c[:4])

c[0].swapcase()
print(c)

