n=input()
s=input()
for i in range(len(n)):
    if n[i]==s:
        print("True")
        print(i)
        break
else:
    print("False")
    