f = open('./tmp/hela.txt', 'w')
f.write('You say good bye, I say hello.')
f.close()

with open('./tmp/hela.txt', 'rb') as f:
    l = f.readline()
    print(l)


