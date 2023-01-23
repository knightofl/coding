list1 = sorted("AsDFghJkLQwRtYu")
print(list1)

list2 = max(list1) + min(list1)
print(list2)

print(eval("12354+56787"))
print(type(eval("12354+56787")))

print(ord('r'), chr(100))

print(list(zip([1,2,3,4,5], [11,22,33,44,55], [111,222,333,444,555])))

print(list(map(lambda x: x*2, 'abcdefg')))

list3 = [-1,0,4,-6,9,-4,10]
print(list(filter(lambda x: x<0, list3)))