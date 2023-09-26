f = open('./tmp/hela.txt', 'w')
for i in range(5):
    f.write('안녕, 매니악맨션.\n')
f.close()

f = open('./tmp/hela.txt', 'r')
while True:
    l = f.readline()
    if l:
        print(l)
    else: break
f.close()

f = open('./tmp/hela.txt', 'r')
ls = f.readlines()
print(ls)
f.close()

f = open('./tmp/hela.txt', 'r')
ls = f.read()
print(ls)
f.close()

with open('./tmp/hela.txt', 'r') as f:
    ls = f.read()
    print(ls)
