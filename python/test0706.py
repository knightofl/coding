class Hero:
    def __init__(self, power, speed, inteli):
        if power + speed + inteli != 30:
            print('에러! 능력치의 합은 30이 되어야 합니다.')
            return
        else:
            self.power = power
            self.speed = speed
            self.inteli = inteli

a = Hero(12,12,3)
b = Hero(12,20,30)

print(a.power)
#print(b.power)

