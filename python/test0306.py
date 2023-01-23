srp = {'가위':'보', '바위':'가위', '보':'바위'}

print(srp.keys())
print(srp.values())
print(srp.items())

print(srp['가위'])

srp.update({'찌':'빠', '묵':'찌', '빠':'묵'})
print(srp)

print('보자기' in srp)

del srp['빠']
print(srp)

for k, v in srp.items():
    if v == '가위':
        print(k)

Key = ['a','b','c','d']
Value = [1,2,3,4] 

dic = {}
for i in range(4):
    dic[Key[i]] = Value[i]
    #dic.update({Key[i]:Value[i]})
print(dic)

print(dic.get('a'))
print(dic.get('e'))
#print(dic['e'])