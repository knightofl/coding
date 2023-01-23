import pandas as pd


stu1 = pd.DataFrame({'name':['Kim','Lee','Choi'],
                     'subject':['c', 'python', 'c'],
                     'result':['pass','pass', 'fail']})

stu2 = pd.DataFrame({'name':['Kim','Hwang','Lee','Park'],
                    'language':['c','java','python','python'],
                    'score':[95,85,97,80]})

print(stu1)
print()
print(stu2)
print()

stu = pd.merge(stu1, stu2)
print(stu)
print()

stu = stu1.merge(stu2)
print(stu)
print()

#stu = pd.merge(stu1, stu2, on='subject')
stu = pd.merge(stu1, stu2, left_on=['subject'], right_on=['language'])
print(stu)
print()

stu = pd.merge(stu1, stu2, on='name')
print(stu)
print()

stu = pd.merge(stu1, stu2, on='name', how='outer') #inner
print(stu)
print()

stu = pd.merge(stu1, stu2, on='name', how='right') #left
print(stu)
print()
