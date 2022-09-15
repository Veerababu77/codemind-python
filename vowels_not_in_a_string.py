n=input()
s="aeiou"
l=[]
l1=[]
for i in n:
    if i in s:
        l.append(i)
for j in s:
    if j not in l:
        l1.append(j)
if len(l1)==0:
    print("0")
else:
    print(*l1)
        