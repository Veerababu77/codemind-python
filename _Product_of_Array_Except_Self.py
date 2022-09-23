n=int(input())
l=list(map(int,input().split()))
l1=[]
s=1
for i in l:
    s=s*i
for j in l:
    x=s//j
    l1.append(x)
print(*l1)