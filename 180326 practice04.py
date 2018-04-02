def sum(num1):
    
    n1 = int(num1/1000)
    n2 = int(num1/100 - n1*10)
    n3 = int(num1/10 - n1*100 - n2*10)
    n4 = int(num1 - n1*1000-n2*100-n3*10)
    sumo = n1+n2+n3+n4
    
    return sumo

def max(num2):

    n1 = int(num2/1000)
    n2 = int(num2/100 - n1*10)
    n3 = int(num2/10 - n1*100 - n2*10)
    n4 = int(num2 - n1*1000-n2*100-n3*10)

    max1=n1

    if n2>max1 :
        max1=n2
    if n3>max1 :
        max1=n3
    if n4>max1 :
        max1=n4
    return max1

print('input num ex)____')
abnum = int(input())
print('sum='+str(sum(abnum)))
print('max='+str(max(abnum)))
