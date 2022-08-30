n,m=map(int,input().split())
l=[]
s=0
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
a=n
b=0
for j in range(len(l)):
    for k in range(len(l)):
        if j==k:
            s=s+l[j][k]
        elif j==b and k==a-1:
            s=s+l[j][k]
    b+=1
    a-=1
print(s)
            