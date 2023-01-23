a = {"a":1, "b":3, "c":5}

try:
    print(a["d"])
except KeyError as e:
    print('예외가 발생했습니다.')
    print(e)

try:
    print(4/0)
except ZeroDivisionError as e:
    print('분모가 0 입니다.')
    print(e)

try:
    print(k)
except NameError as e:
    print('선언되지 않은 변수')
    print(e)

try:
    print(k)
except (NameError, KeyError, ZeroDivisionError) as e:
    print('다시 코딩하시오')
    print(e)

try:
    f = open('./tmp/sample.txt', 'w')
except:
    pass
finally:
    f.close()


class Test:
    def test(self):
        raise NotImplementedError

class Test1(Test):
    def test(self):
        print('자식 클래스 메소드 오버라이딩')

aaa = Test1()
aaa.test()