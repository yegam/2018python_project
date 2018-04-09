def 곱셈(num1,num2) :
     return num1*num2

def 덧셈(num1,num2) :
    return num1+num2

def 나눗셈(num1,num2) :
    return int(num1/num2)

def 뺄셈(num1,num2) :
    return num1-num2

selectList=[1,2,3,4,5,]

print('******기본 계산기 프로그램******')
print('초기 숫자를 입력하세요.')
num1=int(input())
while True :
    print('계산기 숫자를 입력하세요. 1.곱셈 2.덧셈 3.나눗셈 4.뺄셈 5.출력')
    select=int(input())
    if select !=5 :
        print('연산할 숫자를 입력하세요.')
        num2 = int(input())
        if select == 1 :
            num1 = 곱셈(num1,num2)
        elif select == 2 :
            num1 = 덧셈(num1,num2)
        elif select == 3 :
            num1 = 나눗셈(num1,num2)
        elif select == 4 :
            num1 = 뺄셈(num1,num2)
    else :
        print(num1)
        break
    print('연산 후 num1=%d'%num1)
