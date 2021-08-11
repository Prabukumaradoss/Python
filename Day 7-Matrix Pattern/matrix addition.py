matrix_1=[]
matrix_2=[]
sum=[]
for i in range(3):
    matrix_1.append([])
    for j in range(3):
        matrix_1[i].append(int(input(f"Enter element {i}{j} = ")))
        
for i in range(3):
    matrix_2.append([])
    for j in range(3):
        matrix_2[i].append(int(input(f"Enter element {i}{j} = ")))

for i in range(3):
    for j in range(3):
        sum=matrix_1[i][j]+matrix_2[i][j]
        print(sum,end=" ")
    print()










        
#for i in range(3):
 #   sum.append([])
  #  for j in range(3):
   #     sum[i].append(matrix_1[i][j]+matrix_2[i][j])
        
#for i in sum:
 #   for j in i:
  #      print(j,end=" ")
   # print()



