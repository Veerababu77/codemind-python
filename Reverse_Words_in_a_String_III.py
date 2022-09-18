n=input().split()
s=""
for i in n:
    i=list(i)
    i=i[::-1]
    r=""
    for j in i:
        r=r+str(j)
    s=s+" "+r
print(s[1:])