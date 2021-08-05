b=1
for i in range(5,0,-1):
    for j in range(0,b):
        print(i,end=" ")
        i+=1
    if b<5:
        b+=1
    print()
