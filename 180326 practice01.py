#별찍기 테스트
n=1
while n<6 :
    i=0
    k=0
    while i<8-(n-1)*2 :
        print('  ',end='')
        i+=2
    while k<1+(n-1)*2 :
        print('* ',end='')
        k+=1
    n+=1
    print()
