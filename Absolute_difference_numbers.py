n,m=map(int,input().split())
n=str(n)
a=len(n)-1
s=""
s1=""
for i in range(m):
    s=s+n[i]
    s1=n[a]+s1
    a-=1
    i+=1
s=int(s)
s1=int(s1)
print(abs(s-s1))
    
    