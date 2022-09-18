n=int(input())
for i in range(n):
    x="0123456789"
    s=input()
    c=0
    for i in s:
        if i not in x:
            c+=1
            break
    if c==0:
        print("True")
    else:
        print("False")