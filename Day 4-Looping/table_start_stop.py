n=int(input("Enter table number: "))
i=int(input("Enter starting number of Table"))
j=int(input("Enter ending number of Table"))
if i<j:
    for i in range(i,j+1,1):
        print(f"{i}x{n}={i*n}")
else:
     for i in range(i,j-1,-1):
         print(f"{i}x{n}={i*n}")
    
         
