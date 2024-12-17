#Количество совпадающих пар
a = input().split()
c = 0
b = 0
for i in range(len(a)):
    if a.count(a[i])==2:
        b+=1
    if a.count(a[i])!=2:
        c+=a.count(a[i])//2
print(c+b//2)