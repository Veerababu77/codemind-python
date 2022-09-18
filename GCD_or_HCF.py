a,b=map(int,input().split())
l=[]
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
for j in range(b,0,-1):
    if b%j==0 and j in l:
        print(j)
        break