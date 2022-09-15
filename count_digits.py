n=int(input())
l=list(map(int,input().split()))
#print(l)
li=[]
for i in l:
    if i<0:
        i=i*(-1)
    i=str(i)
    li.append(len(i))
print(*li)