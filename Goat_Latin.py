n=input().split()
s=""
v="aeiouAEIOU"
c=1
a=v[0]
for i in n:
    x=i[0]
    if x in v:
        i=i+"ma"+(c*a)
        s=s+" "+i
        c+=1
    else:
        x=i[0]
        i=i[1:]
        i=i+x+"ma"+(c*a)
        s=s+" "+i
        c+=1
print(s[1:])