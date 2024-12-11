#Максимальное число, идущих подряд элементов
b=0
c=1
k=0
a = int(input())
while a!=0:
    b=a
    a = int(input())
    if a==b:
        c+=1
    if c>k:
        k=c
    if a!=b:
        c=1
        b=a
print(k)