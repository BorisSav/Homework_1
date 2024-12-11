#Индекс максимума последовательности
b=0
c=0
d=0
a = int(input())
while a!=0:
    if a>b:
        b=a
        d=c
    a = int(input())
    c+=1
print(d)