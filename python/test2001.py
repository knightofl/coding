class mulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy

class addLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy


apple, orange = 100, 150
a, o = 2, 3
tax = 1.1

mulApple = mulLayer()
mulOrange = mulLayer()
addAppleOrange = addLayer()
mulTax = mulLayer()

applePrice = mulApple.forward(apple, a)
orangePrice = mulOrange.forward(orange, o)
allPrice = addAppleOrange.forward(applePrice, orangePrice)
price = mulTax.forward(allPrice, 1.1)

print(price)
print(mulTax.backward(price))
