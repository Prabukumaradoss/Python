for i in range(5):
    for j in range(5):
        if j==0 or i==j or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
