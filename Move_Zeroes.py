n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i==0:
        l.remove(i)
        l.append(0)
print(*l)