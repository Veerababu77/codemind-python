n=input()
n=n.lower()
n=list(n)
m=input()
m=m.lower()
m=list(m)
c=""
x=0
for i in range(len(n)):
    if n[i] in m and n[i] not in c and n[i]!=" ":
        c+=str(n[i])
        x+=1
if x==0:
    print(-1)
else:
    c=set(c)
    c=list(c)
    c.sort()
    for i in range(len(c)):
        print(c[i],end="")
    
