#Длина отрезка
def distance(x1, y1, x2, y2):
    a=(x1-x2)**2
    b=(y1-y2)**2
    return (a+b)**(1/2)
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))