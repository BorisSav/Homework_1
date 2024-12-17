#Шеренга
a = input().split()
X = int(input())
c=0
for i in range(len(a)):
    if X <= int(a[i]):
        c = i + 1
print(c+1)