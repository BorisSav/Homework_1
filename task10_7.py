#Переставить min и max
a = [int(s) for s in input().split()]
ma=a[0]
mi=a[0]
ca=0
ci=0
for i in range(len(a)):
    if a[i]>ma:
        ma=a[i]
        ca=i
    if a[i]<mi:
        mi=a[i]
        ci=i
a[ca],a[ci]=a[ci],a[ca]
print(*a)