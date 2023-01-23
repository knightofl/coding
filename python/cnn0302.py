name = '둘리'
age = 10000

f1 = 'name: ' + name + ', age: ' + str(age)
print(f1)

f2 = 'name: ' + format(name, 's') + ', age: ' + format(age, 'd')
print(f2)

f3 = 'name: {}, age: {}'
print(f3.format(name, age))

f4 = 'name: {1}, age: {0}'
print(f4.format(age, name))

f5 = f'name: {name}, age: {age}'
print(f5)

