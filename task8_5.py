a = input()
print(a[0:a.find('h')],a[a.rfind('h'):a.find('h'):-1],a[a.rfind('h'):len(a)],sep='')