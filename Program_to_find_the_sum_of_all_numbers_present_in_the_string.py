n=input()
s="0123456789"
sm=0
for i in n:
    if i in s:
        sm+=int(i)
print(sm)
    