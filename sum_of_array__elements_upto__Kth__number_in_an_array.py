n=int(input())
l=list(map(int,input().split()))
x=int(input())
s=0
for i in l:
    if i==x:
        break
    else:
        s+=i
print(s+x)
        