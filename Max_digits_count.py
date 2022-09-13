n=int(input())
l=list(map(int,input().split()))
s=max(l)
s=str(s)
v=0
for i in l:
    if len(str(i))==len(s):
        v+=1
print(v)