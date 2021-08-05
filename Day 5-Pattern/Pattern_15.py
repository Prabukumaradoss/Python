b=0
for i in range(5,0,-1):
    a=i
    print(a,end=" ")
    for j in range(1,5):
        if j%2!=0:
            a=a+1
            c=a+b
            if c<10:
                 print(f"{ c}",end=" ")
            if c>=10:
                print(f"{c}",end=" ")
        if j%2==0:
            a=a+9
            if a<10:
                 print(f"{ a}",end=" ")
            if a>=10:
                print(f"{a}",end=" ")
    print("")
    b+=2
