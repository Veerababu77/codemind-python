n=int(input())
l=list(map(int,input().split()))
le=[]
for i in l:
    if i not in le:
        le.append(i)
print(sum(le))