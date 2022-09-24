n=int(input())
if n<=2:
    print("The pattern is not possible")
else:
    c=0
    for i in range(1,n+1):
        print(i*("*"))
        c+=1
        if c==n:
            for j in range(n-1,0,-1):
                print(j*("*"))
    