dic = {"a":1, "b":2, "c":3, "d":4}

print(dic.keys())
print(dic.values())
print(dic.items())

print('e' in dic.keys())
print(5 in dic.values())

ddd = {'group': None, 'name': None, 'age': None, 'area': None}
print(ddd)

for i in ddd:
    ddd[i] = input('%s : '%i)

print(ddd)

for k,v in ddd.items():
    print('내 %s는 %s입니다' % (k, v))

