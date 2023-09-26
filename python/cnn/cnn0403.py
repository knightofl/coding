animal = ['cat', 'cow', 'dog', 'tiger', 'lion']

for an in animal:
    print(an)
    if an == 'dog':
        break
else:
    print('krrrr')


seq = range(100)
print(seq, type(seq))


for i in range(0, 10, 2):
    print(i, end=' ')
else:
    print()

for i in range(10, 0, -2):
    print(i, end= ' ')
else:
    print()


sum = 0
for i in range(1, 11):
    sum += i
print(sum)


for i in range(5, 0, -1):
    print('*' * i)

for i in range(1, 10, 2):
    print(' '*((9-i)//2) + '*'*i)


for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j} * {i} = {i*j}', end='\t')
    else:
        print()


n = 10
while (n>0):
    print(n, end=' ')
    n -= 1
else:
    print('end')


animal.sort(reverse=True)
print(animal)