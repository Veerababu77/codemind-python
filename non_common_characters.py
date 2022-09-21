n=input()
n=n.lower()
n=list(n)
m=input()
m=m.lower()
m=list(m)
c=[]
for i in range(len(n)):
    if n[i] not in m and n[i] not in c:
        c.append(n[i])
for j in range(len(m)):
    if m[j] not in n and m[j] not in c:
        c.append(m[j])
c.sort()
s=""
for k in c:
    if k!=" ":
        s+=str(k)
print(s)