v = int(input())
t = int(input())
if v>=0:
    c=v*t%109
if v<0:
    c=109-abs(v)*t%109
if c==109:
    print(0)
else:
    print(c)