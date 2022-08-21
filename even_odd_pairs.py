n=int(input())
l=list(map(int,input().split()))
le=[]
lee=[]
lis=[]
for i in l:
    if i%2==0:
        le.append(i)
    else:
        lee.append(i)
a=(max(len(le),len(lee)))-(min(len(le),len(lee)))
for k in range(a):
    if len(lee)<len(le):
        lee.append("$")
    else:
        le.append("$")
for j in range(len(lee)):
    lis.append(le[j])
    lis.append(lee[j])
for x in lis:
    if x=="$":
        lis.remove(x)
if n%2==1:
    lis.append(0)
print(*lis)
    
    


    