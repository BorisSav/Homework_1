#числа Фибоначчи
n = int(input())
a = 0
b = 1
if n!=0:
    for i in range(2,n+1):
        a, b = b, a+b
    print(b)
else:
    print(0)