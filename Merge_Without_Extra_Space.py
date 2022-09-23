n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=l1+l2
    l3.sort()
    print(*l3)