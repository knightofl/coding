l1 = []
l2 = [1, True, 'python', 3.14, 'c']

print(l2[1])
print(l2[-1])

print(l2[1:3])
print(l2[:])
print(l2[:2])
print(l2[3:])
print(l2[::2])
print(l2[4::-1])
print(l2[-1::-1])

print(l2 * 2)
print(l2 + [1,2,3])

print(len(l2))

print(3.14 in l2)
print(1 not in l2)

del l2[1]
print(l2)

l2[0] = l2[0] + 5
print(l2)

l2[1:1] = [4] # 인서트
print(l2)

l2[0:2] = [5, 9, 3]
print(l2)

l2.append('lisp')
print(l2)

print(l2.pop())
print(l2)
print(l2.pop(0))
print(l2)
print(l2.pop(1))
print(l2)

l2[1:1] = [8, 7, 6]
print(l2)

l2.insert(2, 'lisp')
print(l2)

l2.insert(2, ['apple', 'banana'])
print(l2)

print(l2[::-1])
l2.reverse()
print(l2)

l2.remove(6)
print(l2)