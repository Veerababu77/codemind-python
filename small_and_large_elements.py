n=input().split()
x=n[0]
y=n[-1]
x=list(x)
y=list(y)
x.sort()
y.sort()
print(x[0],y[-1])