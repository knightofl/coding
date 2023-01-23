class superClass:
    def ex(self):
        print('super')

class subClass(superClass):
    def ex(self):
        superClass.ex(self)
        print('sub')

a = subClass()
a.ex()


def isNum(nnn):
    for i in str(nnn):
        if i not in '.0987654321':
            return False
    return True


class Cal:
    def __init__(self, ccc, num1, num2):
        print(ccc, num1, num2)
        if ccc not in '+-*/':
            print("첫번째 인자가 사칙연산이 아닙니다.")
        elif not (isNum(num1) and isNum(num2)):
            print("두번째와 세번째 인자는 숫자여야 됩니다.")
        else:
            self.ccc = ccc
            self.num1 = num1
            self.num2 = num2
    
    def cal(self):
        if self.ccc == '+':
            return self.num1 + self.num2
        elif self.ccc == '-':
            return self.num1 - self.num2
        elif self.ccc == '*':
            return self.num1 * self.num2
        elif self.ccc == '/':
            return self.num1 / self.num2  

b = Cal('*', 3, 8)
print(b.cal())

c = Cal("+/", 4.5, 3.3)
print(c.cal())
