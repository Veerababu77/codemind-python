n=input()
n=list(n)
n.sort()
#print(n)
x=n[-1]
l=[]
for i in range(len(n)):
    if n[i]!=" ":
        s=n.count(n[i])
        l.append(n[i])
        l.append(s)
        v=n.count(x)
        l.append(x)
        l.append(v)
        break
#print(l)
print(*l)
    
        
