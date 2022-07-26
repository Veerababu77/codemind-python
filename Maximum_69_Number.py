num=input()
l=[]
for i in num:
    l.append(int(i))
l.sort(reverse=True)
if 6 in l:
    i=l.index(6)
    l[i]=9
s=""
for i in l:
    s=s+str(i)
print(s)
    