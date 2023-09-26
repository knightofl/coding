import time
import threading

def delay():
    for i in range(5):
        time.sleep(1)
        print(f'delaying : {i+1}')

print('스레드 시작!')

thr = []

for i in range(5):
    t = threading.Thread(target=delay)
    thr.append(t)

for i in thr:
    i.start()

for i in thr:
    i.join()

print('스레드 끝!')