n=int(input())
for i in range(n):
    x=int(input())
    c=1
    j=1
    for j in range(1,x+1):
        c=c*j
    print(c)