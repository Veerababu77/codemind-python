n=input().split()
c=[]
s="aeiou"
for i in n:
    co=0
    for j in i:
        if j in s:
            co+=1
    c.append(co)
print(c.count(max(c)))
            