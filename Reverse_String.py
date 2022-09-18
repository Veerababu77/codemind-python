n=input().split()
c=len(n)-1
for i in range(len(n)//2):
    n[i],n[c]=n[c],n[i]
    c-=1
    i+=1
print(*n)
    