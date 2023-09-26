import random


ans = random.randint(1, 100)
print('1~100 숫자가 결정되었습니다. 맞춰보세요')

for i in range(10):
    try:
        num = int(input(f'{i+1} >> '))
    except:
        print('정수를 입력하세요.')
        continue

    if ans == num:
        print('정답입니다.')
        break
    elif ans > num:
        print('더 높음')
    else:
        print('더 낮음')
        
