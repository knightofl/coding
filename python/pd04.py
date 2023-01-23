import pandas as pd


score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}

score_df = pd.DataFrame(data=score)
print(score_df)
print()

print(score_df.info())
print()

print(score_df.head(3))
print()

print(score_df.tail(2))
print()

print(score_df.sample())
print()

print(score_df.sample(2, random_state=10))
print()

print(score_df.sample(frac=0.5))