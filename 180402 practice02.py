import random

i=1
while True :
    com=random.randint(1,3)
    if com == 3:
        com = 0
    print(com)
    while True:
        print('가위바위보를 입력하세요.')
        me=input()
        if me == '가위':
            me = 1
            break
        elif me == '바위':
            me = 2
            break
        elif me == '보':
            me = 3
            break
        else :
            print('다시 입력하세요.')
    if com<me:
        print(str(i)+'회만에 이겼습니다.')
        break
    else:
        i+=1
