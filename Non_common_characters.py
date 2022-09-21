n=input()
n=n.lower()
n=list(n)
m=input()
m=m.lower()
m=list(m)
s=[]
c=0
for i in range(len(n)):
    if n[i] not in m and n[i] not in s and n[i]!=" ":
        s.append(n[i])
for j in range(len(m)):
    if m[j] not in n and m[j] not in s and m[j]!=' ':
        s.append(m[j])
print(len(s))
    