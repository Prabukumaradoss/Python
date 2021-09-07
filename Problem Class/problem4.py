a=int(input("No. of Prime Numbers"))
count=0
for i in range(1,1000):
    for j in range(2,i):
        if i%j!=0:
            pass
        elif i%j==0:
            break
    else:
        print(f"{i}")
        count+=1
        if count==a:
            break
