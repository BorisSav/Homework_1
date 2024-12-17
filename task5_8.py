#Разворот последовательности
def razv():
    a = int(input())
    if a != 0:
        razv()
    print(a)
razv()