n=int(input())
l=list(map(int,input().split()))
s=0
lis=[]
for i in l:
    if i not in lis:
        lis.append(i)
for j in lis:
    if j%2==1:
        s=s+j
print(s)
        