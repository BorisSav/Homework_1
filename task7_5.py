a = input()
print(a[0:a.find('h')],a[(a.replace('h', 'c', a.count('h')-1)).find('h')+1:len(a)],sep='')