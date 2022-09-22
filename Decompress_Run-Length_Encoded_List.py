n=int(input())
l=list(map(int,input().split()))
#print(l)
l1=[]
for i in range(0,len(l),2):
    x=l[i+1]
    l2=[]
    for j in range(l[i]):
        l2.append(x)
    l1=l1+l2
print(*l1)
        
        