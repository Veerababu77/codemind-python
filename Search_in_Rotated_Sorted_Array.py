n=int(input())
l=list(map(int,input().split()))
x=int(input())
for i in range(len(l)):
    if l[i]==x:
        print(i)
        break
else:
    print(-1)