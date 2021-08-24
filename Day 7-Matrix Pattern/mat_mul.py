a=[]
b=[]
result=0
Matrix_multiplication=[]
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(int(input(f"Enter element{i}{j}:")))
print()
for i in range(2):
    b.append([])
    for j in range(2):
        b[i].append(int(input(f"Enter element{i}{j}:")))

for i in range(2):
    Matrix_multiplication.append([])
    for j in range(2):
        for k in range(2):
            Matrix_multiplication[i][j]+= a[i][k]*b[k][j]
            
        
            
for i in Matrix_multiplication:
    print(*i)
