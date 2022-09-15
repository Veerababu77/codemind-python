n=input()
s="aeiouAEIOU"
l=[]
l1=[]
for i in n:
    if i in s:
        l.append(i)
for k in l:
    if k not in l1:
        l1.append(k)
print(*l1)

    
        