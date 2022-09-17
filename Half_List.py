n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
a=len(l)-1
for i in range(len(l)//2):
    l1.append(l[a])
    l2.append(l[i])
    a-=1
    i+=1
l3=l1+l2
print(*l3)