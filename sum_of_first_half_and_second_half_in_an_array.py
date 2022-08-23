n=int(input())
l=list(map(int,input().split()))
#print(l)
a=n//2
l1=l[0:a]
l2=list(l)
for i in l1:
    if i in l2:
        l2.remove(i)
print(sum(l1))
print(sum(l2))
