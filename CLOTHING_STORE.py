n=int(input())
l=list(map(int,input().split()))
k=l
k=list(k)
k=set(k)
k=list(k)
c=0
for i in k:
    s=l.count(i)
    r=s//2
    c+=r
print(c)