#Уникальные элементы
a = input().split()
for i in range(len(a)):
    if a.count(a[i])==1:
        print(a[i], end=' ')