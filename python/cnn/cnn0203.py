subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

for i in subs:
    for j in verbs:
        for k in objs:
            print(i + ' ' + j + ' ' + k + '.')



def frange(val, base=0.0, step=0.1):
    frg = []
    i = base

    while i < val:
        frg.append(i)
        i += step
    
    return frg

print(frange(2))
print(frange(2.0, 1.0))
print(frange(3.0, 1.0, 0.5))



apart =[[101,102,103,104], [201,202,203,204], [301,302,303,304], [401,402,403,404]]
arrear = [101,203,401,404]

for i in apart:
    for j in i:
        if j not in arrear:
            print('Newspapers Delivery : ', j)



import random

a = random.randint(1, 9)
b = random.randint(1, 9)

print(f'{a} x {b} = ?')

ans = [a*b]
for i in range(8):
    ans.append(random.randint(1,81))
random.shuffle(ans)
print(ans)

cont = True
while(cont):
    try:
        c = int(input('answer? '))
    except:
        print('입력오류')
        continue
    cont = False

if c == a*b:
    print('정답입니다')
else: print('틀렸어요')

