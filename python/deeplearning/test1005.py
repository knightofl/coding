list1 = [7, 3, 5, 2, 0, 6, 1, 4] 
list2 = filter(lambda  x: x%2, list1)
print(list(list2))

list0 = [x for x in list1 if x%2]
print(list0)
print()

list3 = list(map(lambda x: str(x), list1))
list4 = [str(x) for x in list1]
print(list3)
print(list4)
print()

list3.sort()
print(list3)
print()

list5 = list(enumerate(list3))
print(list5)

list6 = [ord(x) for x in list3]
print(list6)

print(sum(list6), sum(list6)/len(list6))
print(max(list6), min(list6), divmod(max(list6), min(list6)))

list7 = dict(zip(list3, list6))
print(list7)

with open('./tmp/test.txt', 'w') as f:
    f.write(str(list7))

with open('./tmp/test.txt', 'r') as f:
    print(f.read())

print(dir(str))


while True:
    aa = input("숫자 : ")
    try:
        bb = float(aa)
        break
    except:
        continue

print('반올림', round(bb, 3))