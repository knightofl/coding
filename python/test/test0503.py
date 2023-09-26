print([x*y for x in range(4,9) for y in range(3,7)])
print((x*y for x in range(4,9) for y in range(3,7)))
print([a for a in range(4,9)])


l1 = [1,2,3]
l2 = [3,4,5]
print((lambda x,y: x+y)(l1, l2))
print([x*y for x in l1 for y in l2])
print((lambda x,y: [a*b for a in x for b in y])(l1, l2))
print((lambda x,y: [a*b for a in x for b in y])([a for a in range(1,4)], [a for a in range(1,4)]))
print()

aa = [1,3,4,6,7,9]

bb = list(filter(lambda x: x>3, aa))
print(list(bb))

cc = list(map(lambda x: x*3, aa))
print(list(cc))

print((lambda x,y: [i*j for i in x for j in y])(aa, bb))

dd = map(lambda x,y: [j*k for j in x for k in y], [aa], [bb])
print(list(dd))
