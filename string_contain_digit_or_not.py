n=input()
s="0123456789"
c=0
for i in n:
    if i in s:
        c+=1
if c>0:
    print("Contains {} digit".format(c))
else:
    print("Doesn't contain digit")
    