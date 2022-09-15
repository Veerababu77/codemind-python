n=input().split()
l=[]
s="aeiou"
for i in n:
    c=0
    for j in i:
        if j in s:
            c+=1
    l.append(c)
print(*l)