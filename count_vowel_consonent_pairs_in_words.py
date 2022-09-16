n=input().split()
#print(n)
c=0
s="AEIOUaeiou"
s1="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
for j in n:
    a=len(j)-1
    for i in range(len(j)//2):
        if j[i] in s and  j[a] in s1:
        #print(n[i],n[a])
            c+=1
            i+=1
            a-=1
        elif j[i] in s1 and  j[a] in s:
        #print(n[i],n[a])
            c+=1
            i+=1
            a-=1
        else:
            a-=1
            i+=1
print(c)
    