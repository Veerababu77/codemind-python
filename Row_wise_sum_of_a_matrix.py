n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
for j in range(len(l1)):
    print(sum(l1[j]),end=" ")