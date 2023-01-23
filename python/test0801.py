import time

def delay():
    for i in range(5):
        time.sleep(1)
        print(f'delaying : {i+1}')

print('시작!')
for i in range(5):
    delay()

print('끝!')