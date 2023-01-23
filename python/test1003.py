class myErr(Exception):
    def __str__(self):
        return '두 수의 나머지는 0'


aa = input('aa : ')
bb = input('bb : ')
cc = int(aa) % int(bb)

if cc == 0:
    raise myErr
else:
    print(cc)

