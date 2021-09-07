n=[]
for i in range(int(input("Enter no of elements"))):
    n.append(int(input("Enter the number")))
n.sort()
for i in n:
    print(i,end=" ")
