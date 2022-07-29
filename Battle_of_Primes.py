n=int(input())
m=int(input())
c=n+m
for i in range(c+1,c+100,1):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
        sm=i
        break
d=sm-c
print(d)
        
    