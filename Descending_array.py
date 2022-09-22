n=int(input())
l=list(map(int,input().split()))
c=0
l.append(0)
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        print("no")
        break
    else:
        c+=1
if c==len(l)-1:
    print("yes")
        