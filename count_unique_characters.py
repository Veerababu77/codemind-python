s=input().lower()
s1=list(s)
cnt=0
for i in s1:
    if s1.count(i)==1 and i!=" ":
        cnt+=1
print(cnt)