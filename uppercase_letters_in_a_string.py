n=input()
#print(n)
x=n
n=n.upper()
c=0
for i in range(len(n)):
    if n[i]==x[i].strip():
        c+=1
print(c)