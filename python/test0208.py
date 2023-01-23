number = [1,2,3,4,5,6,7,8,9,10]
alphabet = ['a','b','c','d','e']

numalp = number + alphabet
print(numalp)

del numalp[9:12]
print(numalp)

numalp.insert(8, [11,12,13])
print(numalp)

numalp[1:4] = [21.22,23]
print(numalp)

numalp.append(100)
print(numalp)

numalp.reverse()
print(numalp)

numalp.insert(3,['ㄱ','ㄴ','ㄷ'])
print(numalp)

numalp.pop(3)
print(numalp)

numalp1=[]
for i in numalp:
    numalp1.insert(0,i)
print(numalp1)

alphabet3 = alphabet * 3
alphabet3.sort()
print(alphabet3)

for i in alphabet3:
    print(i)