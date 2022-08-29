def fun(x):
    s1=x[::-1]
    if x==s1:
        return True
    else:
        return False
n=input()
n=n.lower()
s=list(n.split(" "))
c=0
for i in s:
    if fun(i):
        c+=1
print(c)