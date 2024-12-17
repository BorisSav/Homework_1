#Больше предыдущего
a = input().split()
for i in range(0,len(a)):
    b = int(a[i])
    if b > int(a[i-1]) and i!=0:
        print(b, end=' ')