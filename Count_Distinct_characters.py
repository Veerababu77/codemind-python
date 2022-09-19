n=input()
n=n.lower()
n=list(n)
n=set(n)
n=list(n)
if " " in n:
    print(len(n)-1)
else:
    print(len(n))