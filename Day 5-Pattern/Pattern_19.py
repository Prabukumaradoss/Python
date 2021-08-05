for i in range(5):
    if i%2!=0:
        for j in range(5):
            print(j%2,end=" ")
    if i%2==0:
        for j in range(5):
            print((j+1)%2,end=" ")
    print("")
