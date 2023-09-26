cars = ('sports', 'suv', 'truck')
spec = (('5000cc', '3000cc', '6000cc'), ('후륜', '4륜', '4륜'), ('300km/h', '200km/h', '200km/h'))
carList = []

class Car:
    def __init__(self, name, color, car):
        self.name = name
        self.color = color
        self.car = car

        if car == cars[0]:
            self.baegi = spec[0][0]
            self.gudong = spec[1][0]
            self.speed = spec[2][0]
        elif car == cars[1]:
            self.baegi = spec[0][1]
            self.gudong = spec[1][1]
            self.speed = spec[2][1]
        elif car == cars[2]:
            self.baegi = spec[0][2]
            self.gudong = spec[1][2]
            self.speed = spec[2][2]

def regitCar():
    name = input('차주의 이름 : ')
    color = input('차량의 색깔 : ')
    while True:
        car = input('차의 종류 : ')
        if car in cars:
            car1 = Car(name, color, car)
            carList.append(car1)
            break  

def searchCar():
    name = input('차주의 이름 : ')
    for i in carList:
        if name == i.name:
            print('이름 :', i.name)
            print('색깔 :', i.color)
            print('차종 :', i.car)
            print('배기량 :', i.baegi)
            print('구동 :', i.gudong)            
            print('속도 :', i.speed)                  

while True:
    a = input('''
메뉴
1.차량 등록
2.차주 검색
3.나가기
''')

    if a == '1':
        regitCar()

    elif a == '2':
        searchCar()

    elif a == '3':
        break

    else:
        continue

