def prime_num(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
s=len(str(n))
c=0
if(prime_num(n)==0):
    print("Not Mega Prime")
else:
    while n>0:
        r=n%10
        n=n//10
        if(prime_num(r)==1):
            c+=1
        else:
            print("Not Mega Prime")
            break
    if(c==s):
        print("Mega Prime")
        
    

            