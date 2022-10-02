n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
for j in range(len(l1)):
    if j==0 or j==len(l1)-1:
        s+=sum(l1[j])
    else:
        a=l1[j]
        x=a[0]
        y=a[-1]
        s+=x
        s+=y
print(s)
        
