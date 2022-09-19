n=input()
n=n.lower()
n=list(n)
c=0
for i in range(len(n)):
    if n[i]==" ":
        continue
    s=n.count(n[i])
    if s==1:
        #print(n[i])
        c+=1
print(c)