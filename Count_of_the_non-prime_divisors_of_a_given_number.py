n=int(input())
l=[]
for i in range(1,n+1,1):
    if n%i==0:
        l.append(i)
c=0
s=0
for j in range(len(l)):
    if l[j]==1:
        c+=1
    else:
        v=0
        for k in range(1,l[j]+1):
            if l[j]%k==0:
                v+=1
        if v==2:
            continue
        else:
            c+=1
print(c)
        
    