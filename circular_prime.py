num=int(input())
c=0
s=0
k=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    while num!=0:
        r=num%10
        s=s*10+r
        num=num//10
    for j in range(1,s+1):
        if s%j==0:
            k+=1
    if k==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    
    
    
            
                
