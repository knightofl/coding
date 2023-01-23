sum = 0

for i in range(5):
    sum += int(input('%d번째 숫자를 입력하시오. : ' % (i+1)))

print('총합 : %d, 평균 :%d'%(sum, sum/5))
