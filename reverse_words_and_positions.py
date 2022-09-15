n=input().split()
n.reverse()
#print(n)
s=""
for i in n:
    i=list(i)
    r=""
    for j in i:
        r=j+r
    s=s+" "+r
print(s[1:])