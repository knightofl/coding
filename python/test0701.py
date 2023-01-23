class Person:
    name = 'Default'

    def __init__(self, name):
        self.name = name

    def pID(self):
        print(self.name)


a1 = Person('Kara')
a1.pID()

print(Person.name)
print(a1.name)

a1.name = 'Maria'
a1.pID()

a1.__class__.name = 'Jack'
print(Person.name)
