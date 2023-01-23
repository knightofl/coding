s = 'ham and spam'

s1 = s.split()
print(s1)

s2 = ' '.join(s1)
print(s2)


a = [1, 2, 3]
a.insert(2, 4)
print(a)
a.append(5)
print(a)
a.reverse()
print(a)
a.extend([6, 7])
print(a)
b = a.pop()
print(b, a)
c = a.pop(0)
print(c, a)


a = [1, 2, 3, 4]
a[2] = a[2] + 4
print(a)
a[0:2] = [10, 20]
print(a)
a[0:2] = [5]
print(a)
a[1:2] = [6]
print(a)
a[1:1] = [7]
print(a)
a[5:] = [123]
print(a)
a[:0] = [-1, -2]
print(a)


b = {1, 2, 3}
b.add(4)
print(b)
b.discard(2)
print(b)
b.remove(1)
print(b)
b.update({1,2})
print(b)


t = 10, 20, 30, 'banana'
print(t)
print(type(t))

h,i,j,k = t
print(j,i,j,k)

x,*y = t
print(x, y)
*x,y = t
print(x, y)
x,*y,z = t
print(x, y, z)


a = dict(a=1, b=2, c=3)
print(a)
print(a['b'])

a['d'] = 4
print(a)

print(a.items())
print(a.keys())
print(a.values())

del a['b']
print(a)

