
tShot =30

def menu():
    while True:
        mm = input('''
**************************************
메뉴

아메리카노(A를 눌러주세요.)
라떼(L를 눌러주세요.)
에스프레소(E를 눌러주세요.)
**************************************\n''').lower()

        if mm == 'a' or mm == 'l' or mm == 'e':
            return mm

        print('No Menu!')

while tShot:
    choice = menu()
    if choice == 'l':
        if tShot >= 1:
            tShot -= 1
            print('라떼를 선택하셨습니다.')

    elif choice == 'a':
        if tShot >=2:
            tShot -= 2
            print('아메리카노를 선택하셨습니다.')
        else:
            print('재료가 부족해서 주문이 불가합니다.')

    else:
        if tShot >=3:
            tShot -= 3
            print('에스프레소를 선택하셨습니다.')
        else:
            print('재료가 부족해서 주문이 불가합니다.')
    print('%d 샷이 남았습니다.' % tShot)

print('재료소진으로 마감합니다.')






