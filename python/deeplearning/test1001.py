try:
    print(a)
except Exception as e:
    print('All Errors!')
    print(e)

try:
    f = open('./tmp/kkk.txt')
except FileNotFoundError:
    print('no data')

a = {1:2, 3:4}
try:
    print(a[2])
except KeyError as e:
    print('key error', e)

try:
    int('abc')
except (ValueError, KeyError) as e:
    print(e)

try:
    print(a)
except NameError:
    pass
finally:
    print(int('123'))

try:
    for i in 5:
        print(i)
except TypeError as e:
    print(e)


