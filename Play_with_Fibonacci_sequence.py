n=int(input())
a,b=0,1
l=[0,1]
for i in range(n-2):
    c=a+b
    l.append(c)
    a=b
    b=c
print(*l)