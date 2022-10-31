a=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    if i<0:
        i=i*(-1)
    s=str(i)
    t.append(len(s))
print(*t)
