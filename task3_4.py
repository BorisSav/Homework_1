A = int(input())
B = int(input())
if A%2==1:
    for i in range(A,B-1,-2):
        print(i, end=' ')
else:
    for i in range(A-1,B-1,-2):
        print(i, end=' ')