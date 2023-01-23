import copy


a = [1, 2, 3]
b = a # 레퍼런스 카피
c = copy.copy(a) # 얕은 카피
d = copy.deepcopy(a) # 깊은 카피
e = a[:] # 얕은 카피

print(id(a), id(b), id(c), id(d), id(e))
print(a is b)
print(a is c)
print(a is d)
print(a is e)


h = [1, [4, [5, 6]], 2, 3]
i = h # 레퍼런스 카피
j = copy.copy(h) # 얕은 카피
k = copy.deepcopy(h) # 깊은 카피
l = h[:] # 얕은 카피

print(id(h), id(i), id(j), id(k), id(l))
print(id(h[1]), id(i[1]), id(j[1]), id(k[1]), id(l[1]))
print(id(h[1][1]), id(i[1][1]), id(j[1][1]), id(k[1][1]), id(l[1][1]))
print(id(h[1][1][1]), id(i[1][1][1]), id(j[1][1][1]), id(k[1][1][1]), id(l[1][1][1]))

print(h is i)
print(h is j)
print(h is k)
print(h is l)

print(h[1] is i[1])
print(h[1] is j[1])
print(h[1] is k[1])
print(h[1] is l[1])
