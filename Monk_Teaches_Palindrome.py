n=int(input())
for i in range(n):
    l=input()
    l=list(l)
    #print(l)
    x=l[::-1]
   # print(x)
    s=len(l)
    if l==x and s%2==0:
        print("YES EVEN")
    elif l!=x:
        print("NO")
    else:
        print("YES ODD")