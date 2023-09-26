deposit = 10000
print ('총액 : %d' % deposit)

def mio():
    while True:
        mm = input('금액을 입력하세요. : ')
        if mm.isdecimal():
            return int(mm)
    #return int(input('금액을 입력하세요. : '))

while deposit > 0:
    io = input('입금 또는 출금을 선택하세요 : ')

    if  io == '입금':
        deposit += mio()
    elif io == '출금':
        mm = mio()
        if deposit >= mm:
            deposit -= mm
        else: print('잔고가 모자랍니다.')

    print ('총액 : %d\n' % deposit)

print('통장을 파기합니다.')
