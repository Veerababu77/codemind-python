n=int(input())
s=list(map(int,input().split()))
c=0
c1=0
for i in range(len(s)-1):
    if s[i-1]<s[i] and s[i]>s[i+1] or s[i-1]>s[i] and s[i]<s[i+1]:
        c+=1
    else:
        c1+=1
        break
if c1==1:
    print('no')
else:
    print('yes')