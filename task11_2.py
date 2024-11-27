a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a==c+2 or a==c-2) and (b==d+1 or b==d-1)) or ((b==d+2 or b==d-2) and (a==c+1 or a==c-1)):
    print("YES")
else:
    print("NO")