n=input()
n=n.lower()
n=list(n)
n.sort()
s=""
for i in range(len(n)):
    if n[i]==" ":
        continue
    x=n.count(n[i])
    if x==1:
        s+=n[i]

print(s)