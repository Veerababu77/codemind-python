n=int(input())
l=list(map(int,input().split()))
#print(l)
a,b=map(int,input().split())
#print(a,b)
l1=[]
c=0
for i in l:
    if i>=a and b>=i:
        l1.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(min(l1))
