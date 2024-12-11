#Второй максимум
a = int(input())
b=0
c=0
while a!=0:
    if a>b:
        c,b=b,a
    if a<b and a>c:
        c=a
    a = int(input())
print(c)