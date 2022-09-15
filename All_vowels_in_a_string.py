n=input()
l=[]
s="aeiou"
x=0
for i in n:
    if i not in l:
        l.append(i)
for j in l:
    if j in s:
        x+=1
if x==len(s):
    print("True")
else:
    print("False")
        
