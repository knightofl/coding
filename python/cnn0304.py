s = {1, 2, 3, 7, 8}

print(s, type(s))
print(len(s))
print(5 in s)
print(5 not in s)

s.add(2)
print(s)

s.remove(2)
print(s)

s.discard(3)
s.discard(4)
print(s)

s.update({5, 6})
print(s)

s.clear()
print(s)



s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {10,20,30,40,50}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1.difference(s2))
print(s1.symmetric_difference(s2))


a = map(lambda  x: x**2, [1,2,3,4])

print(a, type(a))
#print(tuple(a))
print(list(a))