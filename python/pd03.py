import pandas as pd


score = {'name': ['Jessi', 'Emma', 'Alex', 'Tom'],
         'score': [100, 95, 80, 85],
         'grade': ['A', 'A', 'B', 'B']}     
i = ['a', 'b', 'c', 'd']
c = ['score', 'grade', 'name', 'email']

df = pd.DataFrame(data=score, index=i, columns=c)
print(df)
print()
