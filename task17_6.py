#Стандартное отклонение
b = 0
c = 0
n = []
m=0
a = int(input())
n.append(a)
while a != 0:
    c+=1
    b+=a
    a = int(input())
    n.append(a)
for i in range(len(n)-1):
    m += (n[i]-b/c)**2
print((m/(c-1))**(1/2))