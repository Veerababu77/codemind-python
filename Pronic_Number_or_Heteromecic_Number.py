n=int(input())
for i in range(n):
    r=i*(i+1)
    if r==n:
        print("YES")
        break
else:
    print("NO")