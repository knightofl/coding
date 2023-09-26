import os, sys

ret = os.fork()
if ret == 0:
    print("자식 프로세스 pid={}, 부모 프로세스 pid={}".format(os.getpid(), os.getppid()))
    exit()
elif ret > 0:
    print("부모 프로세스 pid={}, 자식 프로세스 pid={}".format(os.getpid(), ret))
    exit()

sys.exit(1)
