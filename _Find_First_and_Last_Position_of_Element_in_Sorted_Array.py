n=int(input())
l=list(map(int,input().split()))
x=int(input())
a=len(l)-1
l1=[]
for i in range(0,len(l)):
    if l[i]==x:
        l1.append(i)
if len(l1)!=0:
    print(l1[0],l1[-1],end=" ")
else:
    print(-1,-1,end=" ")
    