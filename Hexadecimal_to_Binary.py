n=int(input())
for i in range(n):
    x=input()
    s=""
    for j in x:
        if j=="0":
            s=s+"0000"
        elif j=="1":
            s=s+"0001"
        elif j=="2":
            s=s+"0010"
        elif j=="3":
            s=s+"0011"
        elif j=="4":
            s=s+"0100"
        elif j=="5":
            s=s+"0101"
        elif j=="6":
            s=s+"0110"
        elif j=="7":
            s=s+"0111"
        elif j=="8":
            s=s+"1000"
        elif j=="9":
            s=s+"1001"
        elif j=="A":
            s=s+"1010"
        elif j=="B":
            s=s+"1011"
        elif j=="C":
            s=s+"1100"
        elif j=="D":
            s=s+"1101"
        elif j=="E":
            s=s+"1110"
        elif j=="F":
            s=s+"1111"
    print(s)