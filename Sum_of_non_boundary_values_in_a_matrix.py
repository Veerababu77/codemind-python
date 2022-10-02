n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
for j in range(len(l1)):
    if j==0 or j==len(l1)-1:
        continue
    else:
        a=l1[j]
        a.remove(a[0])
        a.remove(a[-1])
        s+=sum(a)
print(s)