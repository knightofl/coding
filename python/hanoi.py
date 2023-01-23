def hanoi(disk, start=1, end=3):
    if disk:
        hanoi(disk-1, start, 6-start-end)
        print('%d번 기둥의 %d번 원반을 %d번 기둥에 옮깁니다.' % (start, disk, end))
        hanoi(disk-1, 6-start-end, end)

hanoi(disk=5)
