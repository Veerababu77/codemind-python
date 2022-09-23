n=int(input())
x=int(input())
s=0
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
for j in l:
    s=s+sum(j)
print(s)