class Parents:
    def fun1(self):
        raise NotImplementedError

class Child(Parents):
    pass

ss = Child()
ss.fun1()