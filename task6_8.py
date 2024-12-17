#Числа Фибоначчи
def fib(n):
    p0=0
    p1=1
    if n==1:
        return p1
    if n==0:
        return p0
    if n!=0 and n!=1:
        return fib(n-1)+fib(n-2)
n = int(input())
print(fib(n))