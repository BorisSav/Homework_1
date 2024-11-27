a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a==c+1 and b==d+1) or (a==c-1 and b==d+1) or (a==c+1 and b==d-1) or (a==c-1 and b==d-1) or (a==c and b==d+1) or (a==c and b==d-1) or (a==c+1 and b==d) or (a==c-1 and b==d) or (a==c and b==d):
    print("YES")
else:
    print("NO")
