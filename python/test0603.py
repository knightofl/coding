with open('./tmp/gugu1.txt', 'w') as f:
    for i in range(2, 10):
        for j in range(1, 10):
            f.write('{0} * {1} = {2},'.format(i, j, i*j))


with open('./tmp/gugu2.txt', 'w') as f:
    for i in range(2, 10):
        for j in range(1, 10):
            f.write('{0} * {1} = {2}\n'.format(i, j, i*j))

list1 = []
list2 = []
with open('./tmp/gugu1.txt', 'r') as f:
    while True:
        temp = f.readline()
        if temp:
            list1.append(temp)
        else:
            break
print (list1)

with open('./tmp/gugu2.txt', 'r') as f:
    list2 = f.readlines()    
print (list2)



with open('./tmp/gugu1.txt') as f:
    txt = f.read()

list1 = txt.split(',')
print(list1)

print('.'.join(list1))

