n=int(input())
l=list(map(int,input().split()))
for j in range(max(l),0,-1):
    c=0
    for k in l:
        if k%j==0:
            c+=1
    if c==len(l):
        print(j)
        break

    