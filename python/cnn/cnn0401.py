t1 = ()
print(t1, type(t1))

t2 = (1)
print(t2, type(t2))

t3 = (1,)
print(t3, type(t3))

t4 = (1, 2, 3, 4, 5, 6)
print(t4[1])
print(t4[-3:-1])
print(t4[-1::-1])
print(t4 * 2)

print(t4.index(6))
print(t4.count(1))

x = 1, 2, 3
print(x, type(x))

x, y, z = 10, 20, 30
print(x, y, z)

x, y = y, x
print(x, y)

x, *y, z = 10, 20, 30, 40
print(x, y, z)
print(*y)

