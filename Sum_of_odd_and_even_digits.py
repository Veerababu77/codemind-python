n=int(input())
l=list(map(int,input().split()))
od=0
ev=0
for i in range(len(l)):
    if i%2==0:
        od+=l[i]
    else:
        ev+=l[i]
if (od-ev)==0:
    print("YES")
else:
    print("NO")