n=int(input())
l=list(map(int,input().split()))
lis=[]
c=0
for i in l:
    if i%2==1 and i not in lis:
        lis.append(i)
        c+=1
print(c)

