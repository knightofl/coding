for k,v in {'one':1, 'two':2}.items():
    print(k, v)


def rev(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for c in rev('hello'):
    print(c)

print(list(rev('hello')))


print([i*2 for i in range(5)])

ll = [(1,2), (2,3), (2,4), (3,4)]

print({i**j for i,j in ll})

a = [1,2,3,4,5,3,5,6,4,2,6,7,8,4,7,9]
print(a)

while 3 in a:
    a.remove(3)
print(a)
