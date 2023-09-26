class Person:
    '부모 클래스'
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def pInfo(self):
        print(f'이름 : {self.name}, 전화 : {self.phone}')

class Student(Person):
    def __init__(self, name, phone, sub, id):
        super().__init__(name, phone)
        self.sub = sub
        self.id = id

    def pInfo(self):
        super().pInfo()
        print(f'전공 : {self.sub}, 아이디 : {self.id}')

class Teacher(Person):
    def __init__(self, name, phone, sex, age):
        super().__init__(name, phone)
        self.sex = sex
        self.age = age

    def pInfo(self):
        super().pInfo()
        print(f'성별 : {self.sex}, 나이 : {self.age}')


a1 = Student('lee', '010', 'math', 'eagle')
print(a1.name)

a2 = Teacher('kim', '011', 'male', 35)
print(a2.age)

a2.pInfo()
a1.pInfo()