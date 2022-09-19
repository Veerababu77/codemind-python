n=int(input())
t=n
s=0
while n:
    r=n%10
    n=n//10
    c=1
    for i in range(1,r+1):
        c=c*i
    s+=c
if t==s:
    print("The number {} is a strong number".format(t))
else:
    print("The number {} is not a strong number".format(t))

    
        
        