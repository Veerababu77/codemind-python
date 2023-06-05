n=int(input())
s=list(map(int,input().split()))
cn=0
for i in range(1,n-1,2):
    if s[i-1]<s[i] and s[i]>s[i-1]:
        cn+=1
    else:
        print("-1")
        cn=0
        break
if cn!=0:
    print(cn)