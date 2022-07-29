import math as m
def primes(n):
    if n<2:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
x=0
for s in range(a,b+1):
    if primes(s):
        x=x+1
print(x)