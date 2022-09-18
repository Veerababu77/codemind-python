n=int(input())
l=[]
for i in range(n+1):
    c=n-(2**i)
    if c<=0:
        c=c*(-1)
        l.append(c)
    else:
        l.append(c)
#print(l)
print(min(l))
        
    