class CounterManager:
    insCount = 0
    def __init__(self):
        CounterManager.insCount += 1
    
    def __del__(self):
        CounterManager.insCount -= 1

    def staticPrintCount():
        print('Instance Count:', CounterManager.insCount)

    sPrintCount = staticmethod(staticPrintCount)

    def classPrintCount(cls):
        print('Instance Count:', cls.insCount)

    cPrintCount = classmethod(classPrintCount)

a = CounterManager()
CounterManager.sPrintCount()
CounterManager.cPrintCount()

b = CounterManager()
CounterManager.sPrintCount()
CounterManager.cPrintCount()

c = CounterManager()
CounterManager.sPrintCount()
CounterManager.cPrintCount()
