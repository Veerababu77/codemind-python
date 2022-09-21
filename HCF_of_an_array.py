n=int(input())
l=list(map(int,input().split()))
s=min(l)
m=max(l)
c=0
for i in range(m):
    x=0
    for j in range(len(l)):
        if i!=0 and l[j]%i==0:
            x+=1
    if x==len(l) and c<i:
        c=i
        
print(c)