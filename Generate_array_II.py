n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(len(l)):
    if i%2==0 or i==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
for k in range(len(l2)):
    for j in range(l2[k]):
        l3.append(l1[k])
print(*l3)
    
