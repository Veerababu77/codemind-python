n=input()
c=0
s="0123456789"
for i in n:
    if i in s:
        c+=int(i)
print(c)