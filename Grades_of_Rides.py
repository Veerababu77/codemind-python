x,y,z=map(int,input().split())
a=0
b=0
c=0
if x>50:
    a+=1
if y>60:
    b+=10
if z>100:
    c+=24
if a+b+c==35:
    print(10)
elif a+b+c==11:
    print(9)
elif a+b+c==34:
    print(8)
elif a+b+c==25:
    print(7)
elif a+b+c==1 or a+b+c==10 or a+b+c==24:
    print(6)
else:
    print(5)