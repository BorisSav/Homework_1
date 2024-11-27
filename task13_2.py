N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N<M:
    N,M=M,N
if x>M:
    x,y=y,x
a=abs(N-y)
b=abs(M-x)
print(min(a,b,x,y))