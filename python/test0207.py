print("나는 아침마다 %d잔의 우유를 마시고 %s를 봅니다." % (1, "뉴스"))
print("%-14s" % "hello")
print("%10s" % "bye")
print("%15.3f" % 2.567856)

string1 = "My life is mine."
print(string1)

string2 = string1.upper()
print(string2)

string3 = string1.lower()
print(string3)

string4 = string1.swapcase()
print(string4)

string5 = string1.capitalize()
print(string5)

string6 = string1.title()
print(string6)

print('string2 에서 M의 갯수는 %d' % string2.count('M'))

print('string2 에서 M이 처음 나오는 자리는 %d' % string2.find('M'))

print(';'.join('12345'))

add = "192.168.100.40"
print(add.split('.'))

text = 'abcde'
print(' '.join(text).split())
