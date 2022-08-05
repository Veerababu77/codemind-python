n=int(input())
l=list(map(int,input().split()))
#print(l)
sm=sum(l)//len(l)
c=0
for i in range(len(l)):
    if l[i]>=sm:
        c+=1
print(c)