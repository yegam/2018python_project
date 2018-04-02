def inputnum(num):
    absolute=0
    factorial = num
    i=1
    if 2<=num<5 :
        while i<num :
            factorial = factorial*(num-i)
            i+=1
        return factorial
    else :
        absolute = abs(num)
        return absolute

print('input num')
num=int(input())
out=inputnum(num)
print(out)
