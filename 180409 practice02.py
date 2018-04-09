print('숫자를 입력하세요.(1~100까지)')
ran = int(input())
for i in range(1,ran+1) :
    cnt = 0
    if i<10 :
        if i%3 == 0 :
            cnt += 1
    elif 10<=i<100 :
        if (i%10)%3 == 0 and (i%10) != 0:
            cnt += 1
        if (int(i/10))%3 == 0:
            cnt += 1

    if cnt>0 :
        p='-'*cnt
        print('%s '%p,end='')
    else :
        print('%d '%i,end='')
