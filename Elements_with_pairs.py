n=int(input())
l=list(map(int,input().split()))
if n%2==1:
    l.append(0)
print(*l)