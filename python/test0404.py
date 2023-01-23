srp1 = ['가위','바위','바위','바위','보','가위','가위','보','가위','보']

srp2 = input('가위 바위 보! : ')

win = lose = draw = 0

for i in srp1:
    print('%s 대 %s' % (srp2, i), end= ' ')

    if srp2 == i:    
        draw += 1
        print('무')
    elif (srp2 == '가위' and i == '보') |\
        (srp2 == '바위' and i == '가위') |\
        (srp2 == '보' and i == '바위'):
        win += 1
        print('승')
    else:
        lose += 1
        print('패')

print("%d승 %d무 %d패" % (win, draw, lose))