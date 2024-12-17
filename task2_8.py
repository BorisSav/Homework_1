#Отрицательная степень
def power(a,n):
    if n>0:
        c=a
        for i in range(n-1):
            a*=c
    if n<0:
        c=a
        a=1
        for i in range(abs(n)):
            a/=c
    if n==0:
        a=1
    return a
a = float(input())
n = int(input())
print(power(a,n))