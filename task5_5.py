a = input()
if a.count('f')==1:
    print(a.find('f'))
if a.count('f')>1:
    print(a.find('f'),(a.replace('f', 'c', a.count('f')-1)).find('f'))