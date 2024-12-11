#Степень двойки
a = int(input())
b=1
c=0
while b<a:
    b=b*2
    c+=1
if a<b:
    print(c-1,b//2)
else:
    print(c,b)