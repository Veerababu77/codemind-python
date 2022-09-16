n=input()
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=0
for i in n:
    i=i.strip()
    if i not in s:
        c+=1
print(c)