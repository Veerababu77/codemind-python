n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
s=0
for i in range(len(l1)):
    s+=sum(l1[i])
print(s)