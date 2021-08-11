matrix=[]
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(int(input(f"Enter element {i}{j} = ")))
        
for i in range(3):
    for j in range(3):
        if i==j or i+j==2:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

                             
