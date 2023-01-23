print((lambda x: x*2)(5))

print((lambda a, b: a+b)(4,6))

print((lambda a, b: (a+b, a*b))(4,6))


list1 = [2, 3, 4]
list2 = [4, 5, 6]
list3= []

print((lambda x, y: [i*j for i in x for j in y])(list1, list2))
print((lambda x,y: x*y)(4,5))
