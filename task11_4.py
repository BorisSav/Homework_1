b=0
c=0
N = int(input())
for i in range(N-1):
    a = int(input())
    b+=i
    c+=a
print(b+2*N-1-c)