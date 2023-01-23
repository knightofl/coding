import random

srp = ['가위', '바위', '보']
with open('./tmp/srp.txt', 'w') as f:
    f.write(str(srp))

usrsrp = []
for i in range(10):
    usrsrp.append(random.choice(srp))

with open('./tmp/usrsrp.txt', 'w') as f:
    f.write(str(usrsrp))

win = draw = lose = 0

for i in usrsrp:
    rndsrp = random.choice(srp)
    print (f'{i} 대 {rndsrp}')

    if i == '가위':
        if rndsrp == '가위':
            draw += 1
        elif rndsrp == '바위':
            lose += 1
        else:
            win += 1
    elif i == '바위':
        if rndsrp == '가위':
            win += 1
        elif rndsrp == '바위':
            draw += 1
        else:
            lose += 1
    else:
        if rndsrp == '가위':
            lose += 1
        elif rndsrp == '바위':
            win += 1
        else:
            draw += 1

print(f'{win}승 {draw}무 {lose}패')


            
    

