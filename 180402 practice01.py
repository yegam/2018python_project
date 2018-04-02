import random

i=1
while True :
    lot = [random.randint(1,8),random.randint(9,16),random.randint(17,24),random.randint(25,32),random.randint(33,40),random.randint(40,45)]
    if lot[0]==3 and lot[1]==11 and lot[2]==19 and lot[3]==27 and lot[4]==38 and lot[5]==43:
        print(i)
        break
    else :
        i+=1

#3 11 19 27 38 43 가 당첨되려면 몇 회차정도 소요될지 구하는 프로그램
