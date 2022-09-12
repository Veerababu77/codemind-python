n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    s=0
    while i>0:
        r=i%10
        s+=r
        i=i//10
    c+=s
print(c)