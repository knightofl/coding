a = 10
b = 20


def f1():
    c = 10
    d = 20
    print('f1', locals())

f1()
print('globals', globals())


def f2():
    a = 1
    print('f2', locals())

f2()


def f3():
    global a
    a = 2
    print('f3', locals())

f3()


class MyClass:
    x = 10
    y = 20

print(MyClass.__dict__)
print(f1.__dict__)


import sys
cl1 = MyClass()
print(sys.getrefcount(cl1))

cl2 = cl1
print(sys.getrefcount(cl1))

del cl1
print(sys.getrefcount(cl2))


f1.x = 10
MyClass.x = 10
cl2.x = 10
# 사용자 함수, 클래스, 인스턴스는 심볼테이블도 있고 확장도 된다


#print(print.__dict__)
#print.x = 10 ; 내장함수는 심볼테이블 없고 확장도 안된다
print(int.__dict__)
#int.x = 10 ; 내장 클래스는 심볼테이블 있고 확장 안된다
#내장 클래스로 생성된 객체는 심볼 테이블 없고, 확장 안된다


print(dir())
print(dir(__builtins__))

