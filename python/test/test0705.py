class Tiger:
    def jump(self):
        print('호랑이처럼 점프')

    def cry(self):
        print('호랑이처럼 울기')

class Lion:
    def jump(self):
        print('사자처럼 점프')

    def cry(self):
        print('사자처럼 울기')

class Liger(Tiger, Lion):
    def play(self):
        pass

a = Liger()
a.cry()