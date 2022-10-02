n=int(input())
for i in range(1,n+1):
    l=n*["x"]
    l.insert(i,"0")
    l.remove(l[i-1])
    c=""
    for j in l:
        c+=j
    print(c)