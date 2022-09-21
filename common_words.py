x=input()
x=x.lower()
x=list(x.split(" "))
y=input()
y=y.lower()
y=list(y.split(" "))
for i in range(len(y)):
    if y[i] in x:
        print(y[i],end=" ")