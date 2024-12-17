#Наибольший элемент
a = input().split()
c=int(a[0])
b=0
for i in range(2,len(a)):
    if int(a[i]) > c:
        c = int(a[i])
        b = i
print(c,b)