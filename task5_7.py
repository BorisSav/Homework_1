#Больше своих соседей
a = input().split()
c=0
for i in range(2,len(a)):
    if int(a[i-1]) > int(a[i-2]) and int(a[i-1]) > int(a[i]):
        c+=1
print(c)