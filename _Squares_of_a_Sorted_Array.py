n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    i=i*i
    l1.append(i)
l1.sort()
print(*l1)