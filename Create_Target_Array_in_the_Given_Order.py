n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in range(len(l)):
    x=l[i]
    y=l1[i]
    l2.insert(y,x)
print(*l2)