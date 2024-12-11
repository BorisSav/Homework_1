#Количество четных элементов последовательности
b=0
a = int(input())
while a!=0:
    if a%2==0:
        b+=1
    a = int(input())
print(b)