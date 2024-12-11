#номер числа Фибоначчи
A = int(input())
a = 0
b = 1
n = 1
fib_est=0
if A != 0:
    while b <= A:
        if b == A:
            fib_est=1
            print(n)
        a, b = b, a+b
        n += 1
    if fib_est==0:
        print(-1)
else:
    print(0)