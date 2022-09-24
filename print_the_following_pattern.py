n=int(input())
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=list(l)
for i in range(n):
    for j in range(n):
        print(l[i],end=" ")
    print()