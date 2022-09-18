n,m=input().split()
n=list(n)
m=list(m)
c=0
for i in n:
    if i not in m:
        c+=1
        break
    else:
        m.remove(i)
if c==0:
    print("True")
else:
    print("False")
        