a=int(input())
for j in range(a):
    n,m=map(int,input().split())
    c=0
    for i in range(n,m+1,1):
        t=i
        r=t%10
        if r==2 or r==3 or r==9:
            c+=1
        else:
            continue

    print(c)
    