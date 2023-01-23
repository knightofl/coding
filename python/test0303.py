alph = "abcd efg hijk lmnop qrs tuv wxyz"
number = "1234 567 89"
boy = "BOYS, BE AMBITIOUS"

alph1 = alph.upper()
print(alph1)

string1 = boy + alph1
print(string1)
print(string1.count('B'))
print(string1.index('A'))
print(string1.find('A'))

string2 = string1.replace('BOYS', "girls")
print(string2)
print(string2.swapcase())

print(' '.join(alph).split())
