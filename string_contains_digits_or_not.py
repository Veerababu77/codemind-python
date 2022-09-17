n=int(input())
s="0123456789"
for i in range(n):
    x=input()
    c=0
    for i in x:
        if i in s:
            c+=1
            break
    if c==1:
        print("Yes")
    else:
        print("No")
        
            
    