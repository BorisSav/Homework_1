#Ферзи
stolb=[]
strok=[]
diag1=[]
diag2=[]
c=0
for i in range(8):
    a, b = map(int, input().split())
    stolb.append(a)
    strok.append(b)
    diag1.append(a-b)
    diag2.append(a+b-8)
for i in range(len(stolb)):
    if stolb.count(stolb[i])>1:
        c-=1
    else:
        c+=1
for i in range(len(strok)):
    if strok.count(strok[i])>1:
        c-=1
    else:
        c+=1
for i in range(len(diag1)):
    if diag1.count(diag1[i])>1:
        c-=1
    else:
        c+=1
for i in range(len(diag2)):
    if diag2.count(diag2[i])>1:
        c-=1
    else:
        c+=1
if c==len(strok)+len(stolb)+len(diag1)+len(diag2):
    print('NO')
else:
    print('YES')