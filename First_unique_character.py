n=input()
for i in range(len(n)):
    s=n.count(n[i])
    if s==1:
        print(n[i])
        break
else:
    print(-1)