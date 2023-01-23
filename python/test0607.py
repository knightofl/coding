sub1 = ['국어', '영어', '수학', '생물', '화학']
sub2 = ['1학기중간', '1학기말', '2학기중간', '2학기말']

point = []


def writeData():
    with open('./tmp/exam.txt', 'w') as f:
        for i in point:
            for j in i.values():
                print(j, end=' ', file=f)
            print(file=f)


def inputPoint():
    for i in sub2:
        print(i, "성적입력")
        subPoint = {"시험": i}
        for j in sub1:
            subPoint.update({j : int(input(j+ ': '))})
        point.append(subPoint)

    writeData()


def printPoint():
    with open('./tmp/exam.txt', 'r') as f:
        point = f.read()

    print('시험', end=' ')
    for i in sub1:
        print(i, end=' ')
    print()
    print(point)

    getData()

def getData():
    with open('./tmp/exam.txt', 'r') as f:
        temp = f.read().split('\n')
        temp = temp[:-1]
    print(temp)

 
    for i in temp:
        i = i.split()
        k=0

        subPoint = {"시험": i[k]}
        for j in sub1:
            k+=1
            subPoint.update({j : int(i[k])})
        point.append(subPoint)
    
    print(point)


def searchPoint():
    while True:
        a = input('''
성적 확인
1.시험별 성적
2.시험별 평균
3.과목별 점수
4.나가기
''')

        if a == '1':
            printPoint()

        elif a == '2':
            pass

        elif a == '3':
            pass

        elif a == '4':
            return

        else:
            continue


while True:
    a = input('''
성적관리
1.성적 입력
2.성적 확인
3.나가기
''')

    if a == '1':
        inputPoint()

    elif a == '2':
        searchPoint()

    elif a == '3':
        break

    else:
        continue