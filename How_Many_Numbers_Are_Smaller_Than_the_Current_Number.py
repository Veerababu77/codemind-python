n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if i!=j:
            if l[j]<l[i]:
                c+=1
    l1.append(c)
print(*l1)