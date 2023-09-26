l = []

for i in range(2):
    dic = {}
    for j in range(3):
        k = input('키 : ')
        v = input('값 : ')
        dic.update({k:v})
    print(dic)    
    l.append(dic)
print(l)