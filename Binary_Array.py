n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]<=1:
        continue
    else:
        c+=1
        break
if c==1:
    print("False")
else:
    print("True")
