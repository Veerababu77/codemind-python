n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
c=0
for k in range(len(l1)):
    if c<sum(l1[k]):
        c=sum(l1[k])
print(c)