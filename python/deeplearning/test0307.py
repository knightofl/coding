a = [1,2,3,4]
b = "aabbccddeeff"
print(a)
print(b)

s1 = set(a)
s2 = set(b)
print(s1)
print(s2)

#s1 = s1.union({'a', 'b', 'c'})
s1.update({'a', 'b', 'c'})
print(s1)

s2 = s2.union({1, 2})
print(s2)

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

print(s2 - {1})
#print(s2.remove(1))
