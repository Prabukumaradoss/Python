a=int(input("Print prime numbers from 1 to "))
for j in range(1,a+1):
    for i in range(2,j):
        if j%i!=0:
            pass
        elif j%i==0:
            break
    else:
        print(f"{j}")
                
