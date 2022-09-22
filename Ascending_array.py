n=int(input())
l=list(map(int,input().split()))
z=set(l)
l1=list(z)
l1.sort()
if l1==l:
    print('yes')
else:
    print('no')