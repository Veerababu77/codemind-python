n=input().split()
c=len(max(n))
for i in n:
    if len(i)<c:
        c=len(i)
print(c)