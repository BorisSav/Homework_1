#Количество элементов, которые больше предыдущего
a = int(input())
b=a
c=0
while a!=0:
    a = int(input())
    if a>b:
        c+=1
    b=a
print(c)