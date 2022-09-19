n=int(input())
for i in range(n):
    x=int(input())
    for j in range(x):
        if j*j==x:
            print(True)
            break
    else:
        print("False")
        