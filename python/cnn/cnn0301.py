s = 'i Like python'
print(s.swapcase())
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())

print(s.find('k'))
print(s.rfind('i'))
print(s.index('L'))
print(s.rindex('i'))

print(s.startswith('i'))
print(s.endswith('Python'))
print(s.endswith('python'))
print(s.endswith('Like', 0, 5))
print(s.endswith('Like', 0, 6))


s = 'one:two:three:four:five'
print(s.split(':'))
print(s.split(':', 2))
print(s.rsplit(':', 2))


s = '     spam and ham     '
print('***' + s.strip() + '***')
print('***' + s.rstrip() + '***')
print('***' + s.lstrip() + '***')


s = '<><><spam<>and<>ham><><>'
print(s.strip('<>'))


l = '''1st line
2nd line
3rd line
4th line'''

print(l)
print(l.splitlines())
print(l.split('\n'))


ll = l.splitlines()
print(ll)
print(' & '.join(ll))


print('abcd'.isalpha())
print('1234'.isdecimal())
print('ab12'.isalnum())
print('3²'.isdigit())
print('3²'.isnumeric())
print('abc'.islower())
print('ABC'.isupper())

