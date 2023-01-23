class NumberError(Exception):
    def __str__(self):
        return '숫잔 안됨'


while True:
    try:
        aa = input('문자열 입력 : ')
        if aa.isnumeric():
            raise NumberError
        else:
            print(aa)
            break
    except NumberError as e:
        print(e)
        continue

