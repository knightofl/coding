# 함수
# def 함수명(인자):

def sum(a, b):
    return a+b

print(sum(4, 5))


# 가변인자
def sumx(*params):
    s = 0
    for i in params:
        s = s + int(i)

    return s

print(sumx(1,2,3))

def sumy(*params):
    x = 0
    y = 1
    for i in params:
        x += int(i)
        y *= int(i)

    return x, y
    # 함수의 리턴값이 2개 이상의 변수라면, 리턴값은 튜플

print(sumy(1,2,3,4))


# 함수인자 초기값
def person(name, age, height=100):
    print(name, age, height)

person('Kim', 12)
person('Lee', 18, height=120)
# 기본값 부여된 파라미터는 호출시 명시적으로 지정가능.
# 호출시 인자의 순서를 바꾸는 건 기본값이 모두 지정된 경우에 가능