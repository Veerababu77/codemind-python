n=input()
l=[]
c=0
for i in n:
    if i!=" " and i not in l:
        l.append(i)
    else:
        #print("False")
        c+=1
        break
if c!=0:
    print("False")
else:
    print("True")