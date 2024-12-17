#Большие буквы
def capitalize(a):
    a=a.replace(a[0],chr(ord(a[0])-32))
    for i in range(len(a)):
        if ord(a[i-1])==32:
            a=a.replace(a[i],chr(ord(a[i])-32))
    return a
a = input()
b = a.split()
for i in range(len(b)):
    b[i]=capitalize(b[i])
print(*b)