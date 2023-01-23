class MyClass:
    count = 0
    x = 22

    def __init__(self, y):
        self.y = y
        MyClass.count += 1
        print('클래스 생성', MyClass.count)

    def __del__(self):
        MyClass.count -= 1
        print('클래스 소멸', MyClass.count)


    @staticmethod
    def staticMethod():
        return 'static method!'

    @classmethod
    def classMethod(cls):
        return cls.x


a = MyClass(5)

print(MyClass.staticMethod())
print(MyClass.classMethod())
print(a.y)
del a



class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
    
    def __str__(self):
        return f'"Rect({self.x1}, {self.y1}, {self.x2}, {self.y2})"'

    def __repr__(self):
        return f'Rect({self.x1}, {self.y1}, {self.x2}, {self.y2})'

    def area(self):
        return (self.x2-self.x1) * (self.y2-self.y1)


r1 = Rect(10, 10, 50, 50)
r2 = eval(repr(r1))

print(r1, r1.area())
print(r2, r2.area())

