l1 = [1, 2, 3, 4, 5, 6]
r1 = [a**2 for a in l1]
print(r1)

r2 = map(lambda x: x**2, l1)
print(list(r2))


l2 = ['a', 'as', 'bat', 'cat', 'dove', 'tiger']
r2 = [len(i) <= 2 for i in l2]
print(r2)

r3 = tuple(filter(lambda x: len(x)<=2, l2))
print(r3)

r4 = [s for s in l2 if len(s) <= 2]
print(r4)


for i in range(100):
    s = str(i)
    c = s.count('3') + s.count('6') + s.count('9')

    if c == 1:
        print(i, '짝')
    elif c == 2:
        print(i, '짝짝')


r4 = [n for n in range(100) if str(n).count('3') + str(n).count('6') + str(n).count('9')]
print(r4)


r5 = {s for s in l2 if len(s)>2}
print(r5)


r6 = {s:len(s) for s in l2 if len(s)<3}
print(r6)

