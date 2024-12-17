#Соседи одного знака
a = input().split()
for i in range(0,len(a)):
    b = int(a[i])
    if (b > 0 and int(a[i-1]) > 0 and i!=0) or (b < 0 and int(a[i-1]) < 0 and i!=0):
        print(int(a[i-1]), b)
        break