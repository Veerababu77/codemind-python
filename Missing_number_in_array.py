n=int(input())
for i in range(n):
    x=int(input())
    l=list(map(int,input().split()))
    j=min(l)
    l.sort()
    l2=[]
    for w in range(1,len(l)+1):
        l2.append(w)
    #print(l2)
    if l==l2:
        print(max(l)+1)
    else:
        for k in l:
            if k!=j:
                print(j)
                break
            else:
                j+=1
            