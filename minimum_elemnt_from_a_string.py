n=input()
n=list(n)
n.sort()
s="abcdefghijklmnopqrstuvwxyz"
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(s)):
    if s[i] in n:
        print(s[i])
        break
    elif s1[i] in n:
        print(s1[i])
        break
    
    
    