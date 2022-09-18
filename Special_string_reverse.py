n=input()
s=""
r="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in n:
    if i in r:
        s=s+i
x=""
a=len(s)-1
for j in range(len(n)):
    if n[j] in r:
        x+=s[a]
        a-=1
    else:
        x+=n[j]
print(x)
    
        