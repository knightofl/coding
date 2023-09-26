import pickle

data = {1:'name', 2:'age', 3:'addr'}

with open('./tmp/test.txt', 'wb') as f:
    pickle.dump(data, f)

with open('./tmp/test.txt', 'rb') as f:
    print(pickle.load(f))
  