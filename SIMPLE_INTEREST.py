P,T,R=map(int,input().split())
R=R/100
s=P*(1+(R*T))
i=s-P
print(int(i))