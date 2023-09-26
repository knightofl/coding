num1 = "0,1,2,3,4,5,6,7,8,9,10"
num2 = num1.split(',')

print(num1)
print(num2)

print(num2[3])
print(num2[5:9])
print(int(num2[5]) * int(num2[7]))

num2[6] = '45'
print(num2)

num2[3:6] = ['31','33','34','35','36','37']
print(num2)

num2[9] = '33'
print(num2)

print(num2.index('33'))
while '33' in num2:
    num2.remove('33')
print(num2)

num2.sort()
print(num2)

num2.reverse()
print(num2)

num2.insert(4, ['a1', 'b1', 'c1'])
print(num2)

num2[5] = ['a2', 'b2', 'c2']
print(num2)

a1 = num2.pop(4)
print(a1)
print(num2)

num3 = []
num2.remove(['a2', 'b2', 'c2'])
print(num2)
for i in num2:
    num3.append(int(i))
print(num3)


