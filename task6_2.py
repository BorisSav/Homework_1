a = int(input())
b = int(input())
c = int(input())
if a==b and b==c:
    print(3)
if (a==b and b!=c) or (c==b and b!=a) or (a==c and b!=c):
    print(2)
if a!=b and b!=c and c!=a:
    print(0)