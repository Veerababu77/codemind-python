n=int(input())
for i in range(n):
    l=input()
    t=len(l)
    s=0
    for k in l:
        t=t-1
        s=int(k)*2**t+s
    print(s)