n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
for i in range(len(l)):
    c=l[i]+l1[i]
    l2.append(c)
print(*l2)