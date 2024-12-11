#Количества элементов, равных максимуму
b=0
c=0
a = int(input())
while a!=0:
    if a>b:
        b=a
        c=0
    if a==b:
        c+=1
    a = int(input())
print(c)