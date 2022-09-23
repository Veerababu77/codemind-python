n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l.count(l[i])!=1:
        print(l[i])
        break