#Вставить элемент
a = input().split()
k, c = map(int, input().split())
b = []
for i in range(len(a)):
    if i!=k:
        b.append(a[i])
    if i==k:
        b.append(c)
        b.append(a[i])
if k==len(a):
    b.append(c)
print(*b)