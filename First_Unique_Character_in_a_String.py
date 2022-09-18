n=input()
l=[]
for i in range(len(n)):
    if n.count(n[i])==1:
        print(i)
        break
else:
    print("-1")