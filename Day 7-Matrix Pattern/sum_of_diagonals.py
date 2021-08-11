matrix_1=[]
matrix_2=[]
matrix_sum=[]
sum=0
for i in range(3):
    matrix_1.append([])
    for j in range(3):
        matrix_1[i].append(int(input(f"Enter element {i}{j}: ")))

for i in range(3):
    matrix_2.append([])
    for j in range(3):
        matrix_2[i].append(int(input(f"Enter element {i}{j}: ")))

for i in range(3):
    for j in range(3):
        matrix_sum = matrix_1[i][j] + matrix_2[i][j]
        if i==j or i+j==2:
            sum+=matrix_sum
print(sum)


