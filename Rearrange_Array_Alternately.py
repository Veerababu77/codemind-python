n=int(input())
for i in range(n):
    x=int(input())
    l=list(map(int,input().split()))
    k=sum(l)
    l1=[]
    for j in range(len(l)//2):
        l1.append(max(l))
        l.remove(max(l))
        l1.append(min(l))
        l.remove(min(l))
    if x%2==0:
        print(*l1)
    else:
        c=abs(sum(k)-sum(l1))
        l1.append(c)
        print(*l1)
    
        
