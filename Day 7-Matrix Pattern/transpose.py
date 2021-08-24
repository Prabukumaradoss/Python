matrix=[]
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(int(input(f"Enter element {i}{j} = ")))

print("matrix = ")
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()

print("Matrix transpose = ")       
for i in range(3):
    for j in range(3):
        print(matrix[j][i],end=" ")
    print()
