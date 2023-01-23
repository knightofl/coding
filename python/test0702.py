class tClass:
    def __init__(self, value):
        #self.value = value
        print(f'클래스가 만들어졌어요. value={value}')

    def __del__(self):
        print('클래스 소멸')

tClass(5)



class countClass:
    ct = 0
    def __init__(self):
        countClass.ct += 1
        print('클래스 생성', countClass.ct)

    def __del__(self):
        countClass.ct -= 1
        print('클래스 소멸', countClass.ct)


c = countClass()
print(c)

t = c
print(t.ct)

t = countClass()
