n=int(input())
s=0
s1=0
c=0
while n:
    r=n%10
    c+=1
    n=n//10
    if r%2==0:
        s+=1
    elif r%2==1:
        s1+=1
    if s==1 and s1==1:
        print("Mixed")
        break

if s==c:
    print("Even")
elif s1==c:
    print("Odd")
        
    