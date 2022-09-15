n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<0:
        i=i*(-1)
    i=str(i)
    i=list(i)
    if len(i)==m:
        c+=1
print(c)