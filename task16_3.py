from math import *
P = int(input())
X = int(input())
Y = int(input())
print(int(((X*100+Y)*(1+P/100))//100),floor(round(((X*100+Y)*(1+P/100))%100,11)))