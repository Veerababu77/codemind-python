n=int(input())
l=list(map(int,input().split()))
x=int(input())
l1=[]
ma=max(l)
for i in l:
    if (i+x)>=ma:
        l1.append(True)
    else:
        l1.append(False)
print(*l1)