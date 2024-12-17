#Количество различных элементов
a = input().split()
c=1
for i in range(1,len(a)):
    if int(a[i])>int(a[i-1]):
        c+=1
print(c)