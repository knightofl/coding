name = input("당신의 이름은? : ")
age = input("당신의 나이는? : ")
bday = input("당신의 생일은? : ")

print('당신의 이름은 {}입니다.'.format(name))
print('당신의 나이는 {}이고, {}대입니다.'.format(age, int(age)//10*10))
print('당신의 생일은 {}입니다.'.format(bday))
