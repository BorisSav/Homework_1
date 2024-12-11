#Список квадратов
N = int(input())
a=0
for i in range(int(N**(1/2))):
    a+=1
    print(a**2,end=' ')