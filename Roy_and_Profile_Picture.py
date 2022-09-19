n=int(input())
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    if a<n or b<n:
        print("UPLOAD ANOTHER")
    elif a==b and a>=n:
        print("ACCEPTED")
    else:
        print("CROP IT")