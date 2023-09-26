import keyword


print(keyword.kwlist)
print(len(keyword.kwlist))

dir(__builtins__)
globals()


a = 10
b = 20
c = 10

print(a == b)
print(a is b)
print(a is c)
print(id(a), id(b), id(c))

a, b = b, a
print(id(a))
print(id(b))
print(c.bit_length())


d = 0b10
e = 0o10
f = 0x10
print(d, e, f)

print(bin(22))
print(oct(22))
print(hex(22))


print(True + True)
print(a != 10)
print(5 < a < 15)


print([] or 'logical')
print('operator' or 'logical')
print(None and 1)


g = 2.
print(type(g))
print(g.is_integer())


print(0.002 == 2e-3)


h = 4 + 5j
print(type(h))
print(h.real, h.imag)


print(divmod(10, 4))
print(~127)
print(2 << 3)
print(8 >> 2)
print(3 & 2)
print(3 | 2)
print(3 ^ 2)


print(type('hello'))