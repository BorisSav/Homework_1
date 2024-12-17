#Кегельбан
N, K = map(int, input().split())
keg='I'*N
b = []
c = []
for i in range(K):
    li, ri = map(int, input().split())
    while li<=ri:
        if b.count(li)==0:
            b.append(li)
        li+=1
for i in range(N):
    if b.count(i+1)>0:
        c.append('.')
    else:
        c.append('I')
print(''.join(c))