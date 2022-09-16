n=input().split()
s="aeiouAEIOU"
c=0
for i in n:
    if i[0] in s:
        c+=1
print(c)