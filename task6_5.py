a = input()
if a.count('f')==1:
    print(-1)
if a.count('f')==0:
    print(-2)
if a.count('f')>1:
    print((a.replace('f', 'c', 1)).find('f'))