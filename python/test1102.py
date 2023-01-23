import sys
import pickle
import random

#sys.path.append('c:/')

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

with open('test', 'wb') as f:
    pickle.dump(list1, f)
    pickle.dump(list2, f)
    pickle.dump(list3, f)

with open('test', 'rb') as f:
    temp1 = pickle.load(f)
    temp2 = pickle.load(f)
    temp3 = pickle.load(f)

print(list(zip(temp1, temp2, temp3)))


srp = ('가위', '바위', '보')
for i in range(10):
    print(random.choice(srp))