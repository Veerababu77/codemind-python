n=input()
s="aeiouAEIOU"
c=0
for i in n:
    if i in s:
        c+=1
print(c)