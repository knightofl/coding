a = input('수를 입력하세요 : ')

try:
    a = int(a)
    if a%3:
        print('3의 배수가 아닙니다')
    else:
        print('3의 배수입니다')
except:
    print('정수가 아닙니다')



a = input('수를 입력하세요 : ')

try:
    a = int(a)
    if a%2:
        print('홀수입니다')
    print('짝수입니다')
except:
    print('정수가 아닙니다')



for i in range(1, 10):
    print('*' *i)



for i in range(1,10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j, end='\t')
    print()



a = [1,2,3,4,5,6,7,8,9,10]
num = sum = 0
for i in a:
    if not i%3:
        num +=1
        sum +=i
print('3의 배수의 갯수', num)
print('3의 배수의 합', sum)



a = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
b = input('금액을 입력하세요 : ')

try:
    b = int(b)
    for i in a:
        print(f'{i}원 : {b//i}개')
        b %= i
except:
    print('정수가 아닙니다')



a = []
for i in range(5):
    a.append(int(input(('정수를 입력하세요 : '))))

sum = 0
for i in a:
    sum += i
print(sum, sum/5)



def reverse(string):
    return string[-1::-1]

a = input('문자열을 입력하세요 : ')
print(reverse(a))



price = {'오뎅':300, '순대':400, '만두':500}
menu = input('메뉴: ')

print(f'{menu}가격: {price[menu]}')



a = int(input('숫자를 입력하세요 : '))
sum = 0

while a>0:
    sum += a
    a -= 2
print(sum)
