n=int(input())
c=1
s=0
while n:
    r=n%10
    c=c*r
    s+=r
    n=n//10
print(c-s)