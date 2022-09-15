n=input().split()
l=len(max(n))
s="aeiou"
for i in n:
    c=0
    for j in i:
        if j in s:
            c+=1
    if c<l:
        l=c
print(l)