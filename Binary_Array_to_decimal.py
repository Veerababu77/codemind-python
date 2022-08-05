n=int(input())
l=list(map(int,input().split()))
len=len(l)
sum=0
for i in range(len):
    len=len-1
    sum=sum+(l[i]*2**len)
print(sum)