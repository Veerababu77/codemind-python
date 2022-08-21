n=int(input())
l=list(map(int,input().split()))
s=0
lis=[]
for i in l:
    if i not in lis:
        lis.append(i)
for j in lis:
    if j%2==0:
        s=s+1
print(s)
        