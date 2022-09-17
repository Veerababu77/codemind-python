n=input()
s=input()
x=s+n
x=list(x)
x.sort()
s1=""
for i in x:
    s1=s1+str(i)
print(s1)