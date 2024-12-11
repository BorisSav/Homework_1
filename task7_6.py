#Среднее значение последовательности
b=0
c=0
a = int(input())
while a!=0:
    c+=1
    b+=a
    a = int(input())
print(b/c)