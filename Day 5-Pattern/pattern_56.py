for i in range(1,6):
    m=4
    for j in range(1,i+1):
        if(j==1):
            print(i,end=" ")
            k=i
        else:
            k=k+m
            m-=1
            print(k,end=" ")
    print()
