sub = ('국어', '영어', '수학', '과학', '사회')
adj ={}

for i in sub:
    while True:
        print(i, end='')
        pp = input('점수를 입력하세요. (0~100): ')
        if pp.isdecimal():
            pp = int(pp)
            if 0<= pp <= 100:
                adj.update({i: pp})
                break
sum = 0
print('60점 이상의 과목은 :', end= ' ')
for k,v in adj.items():
    sum += v
    if v >= 60:
        print(k, end= ' ')


print('\n총점은 %d, 평균은 %d' % (sum, sum/5))
