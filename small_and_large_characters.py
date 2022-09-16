n=input().split()
l=[]
for i in n:
    i=list(i)
    i.sort()
    l.append(i[0])
    l.append(i[-1])
print(*l)