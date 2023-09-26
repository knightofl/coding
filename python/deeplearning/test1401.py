def and_gate(x1, x2):
    return (x1 + x2) > 1

print(and_gate(1, 1))
print(and_gate(1, 0))
print(and_gate(0, 1))
print(and_gate(0, 0))
print()


def or_gate(x1, x2):
    return (x1 + x2) > 0

print(or_gate(1, 1))
print(or_gate(1, 0))
print(or_gate(0, 1))
print(or_gate(0, 0))
print()


def nand_gate(x1, x2):
    #return (x1 + x2) < 2
    return not and_gate(x1, x2)

print(nand_gate(1, 1))
print(nand_gate(1, 0))
print(nand_gate(0, 1))
print(nand_gate(0, 0))
print()


def xor_gate(x1, x2):
    #return (x1 != x2)
    return and_gate(or_gate(x1, x2), nand_gate(x1, x2))

print(xor_gate(1, 1))
print(xor_gate(1, 0))
print(xor_gate(0, 1))
print(xor_gate(0, 0))
print()

