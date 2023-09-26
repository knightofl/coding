import pickle

try:
    f = open('addr', 'rb')
    pList = pickle.load(f)
    print(pList)

except:
    f = open('addr', 'wb')
    pList = []

finally:
    f.close()
    
pInfoKey = ['name', 'sex', 'bday', 'phone', 'region']

def inputInfo():
    pInfo = {}
    for i in pInfoKey:
        pInfo.update({i : input(i+ ': ')})

    pList.append(pInfo)
    with open('addr', 'wb') as f:
        pickle.dump(pList, f)
 
    print(pList)

def searchInfo():
    name = input('찾는 이름 : ')
    for i in pList['name']:
        print(i)


    for i in pList:
        if name == i['name']:
            for k in i:
                print(k, i[k])
            print()      

def editInfo():
    name = input('수정할 이름 : ')
    for i in pList:
        if name in i['name']:
            pass
            



while True:
    a = input('''
명부편집
1.정보 입력
2.정보 확인
3.정보 수정
4.나가기
''')

    if a == '1':
        inputInfo()

    elif a == '2':
        searchInfo()

    elif a == '3':
        editInfo()

    elif a == '4':
        break

    else:
        continue