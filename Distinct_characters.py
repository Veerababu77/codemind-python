n=input()
n=n.lower()
n=list(n)
n=set(n)
n=list(n)
n.sort()
c=""
for i in n:
    if i!=' ':
        c=c+i
print(c)