n=int(input())
l=list(map(int,input().split()))
a=len(l)//2
le=[]
for i in range(a):
    le.append(l[i])
    le.append(l[-(i+1)])
if n%2==1:
    le.append(l[a])
    le.append(0)
print(*le)

    