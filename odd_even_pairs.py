n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
lis=[]
for i in l:
    if i%2==1:
        l1.append(i)
    else:
        l2.append(i)
a=(max(len(l1),len(l2)))-(min(len(l1),len(l2)))
for j in range(a):
    if len(l2)<len(l1):
        l2.append("$")
    else:
        l1.append("$")
for k in range(len(l1)):
    lis.append(l1[k])
    lis.append(l2[k])
for x in lis:
    if x=="$":
        lis.remove(x)
if n%2==1:
    lis.append(0)
print(*lis)