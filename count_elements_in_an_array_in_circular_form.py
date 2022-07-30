n=int(input())
l=list(map(int,input().split()))
l.append(l[0])
c=0
for i in range(1,len(l)-1):
    if l[i-1]%2==0 and l[i+1]%2==1:
        c+=1
            
print(c*2)