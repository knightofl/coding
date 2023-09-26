def yield_exam(num):
    for i in range(num, 0 , -1):
        yield i

print(tuple(yield_exam(10)))


def times(a, b):
    return a*b

print(times(2, 3))


def hello():
    print('안녕, 여러분!')

hello()


def tuple_exam(a, b):
    return a+b, a*b

print(tuple_exam(3, 4))


def sum(*a):
    sum = 0
    for i in a:
        sum += i
    return sum

print(sum(2,3))
print(sum(6,7,8,9))


print(hex(id(sum)))
print(sum)

sum_2 = sum
print(sum_2(4,5,6))


def inc(num, step=1):
    return num+step

print(inc(10))
print(inc(10, 5))


def fun(**dic):
    print(dic)

fun(a=1, b=2, c=3)
